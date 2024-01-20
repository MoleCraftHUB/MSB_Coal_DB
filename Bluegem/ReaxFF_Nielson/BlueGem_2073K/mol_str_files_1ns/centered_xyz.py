import os, sys, glob, subprocess
import numpy as np
from ase import Atoms, Atom
from ase.io import read, write
from ase.visualize import view

xyz_files = sorted( glob.glob('mol_*.xyz'), key=lambda x: int(x[4:-4]))

xyz_read = []

for i, xyz_file in enumerate(xyz_files):
	#read xyz file as txt
	txt_read = open(xyz_file,'r')
	txt_lines = txt_read.readlines()
	for l, line in enumerate(txt_lines):
		line_s = line.split()
		if len(line_s)==1 and line_s[0].isdigit():
			Natoms = int(line_s[0])
			start = l
			end = l + Natoms + 2
			xyz_single = txt_lines[start:end]
			#xyz_single_atoms = np.array(sorted([a.split() for a in txt_lines[start+2:end]],key=lambda x:int(x[4])))
			xyz_single_atoms = np.array([a.split() for a in txt_lines[start+2:end]])
			xyz_read.append(xyz_single_atoms)

	number = xyz_file[4:-4]
	images = read(xyz_file,index=':')
	new_images = []
	open_file = open('atomic_idx_%s.txt' % number,'w')
	for j, atoms in enumerate(images):
		pos = atoms.get_positions()
		idx_ref = xyz_read[j][:,4]
		open_file.write(str(j)+' '+' '.join(idx_ref) + '\n')
		cell_l = atoms.get_cell_lengths_and_angles()
		cell_x_half = cell_l[0] / 2
		cell_y_half = cell_l[1] / 2
		cell_z_half = cell_l[2] / 2

		cm_pos = atoms.get_center_of_mass()
		
		shift_x = cell_x_half - pos[0][0]
		shift_y = cell_y_half - pos[0][1]
		shift_z = cell_z_half - pos[0][2]

		new_pos = pos + [shift_x,shift_y,shift_z]
		atoms.set_positions(new_pos)
		atoms.set_cell(cell_l)
		atoms.set_pbc([1,1,1])
		atoms.wrap()
		atoms.center()

		new_images.append(atoms)
		print('write centered_mol_%s_%d.xyz' % (number,j))
		atoms.write('centered_mol_%s_%d.xyz' % (number,j),format='xyz')
	open_file.close()
	#print('write centered_mol_%s.xyz' % number)
	#write('centered_mol_%s.xyz' % number,new_images,format='extxyz')

