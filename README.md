# fdt-nanopore-geometry-selection
Systematic method for nanopore geometry optimization using a fuzzy decision tree approach validated through finite element simulations.

# Nanopore Geometry Selection Using Fuzzy Decision Tree

This repository provides the simulation models and fuzzy decision tree (FDT) implementation for optimizing nanopore geometry in resistive pulse sensing applications.

The method was developed as part of the study:
**"Computational Modeling of Biological Nanopore Geometries using Fuzzy Decision Trees"**  
(Dürdane Yılmaz, Ali Dinler, 2025)

## Contents

- COMSOL Multiphysics model files for simulating particle translocation through conical, cigar-shaped, and hourglass-shaped nanopores.
- Python scripts implementing the fuzzy decision tree (FDT) model using the `scikit-fuzzy` library.
- Sample simulation outputs and fuzzy decision examples for validation.
- Instructions for running simulations and fuzzy model evaluation.

## Purpose

The repository enables reproducibility of the nanopore geometry selection method described in the MethodsX article. Researchers can adapt the models and code for custom nanopore design tasks involving size discrimination, charge sensitivity, and trajectory robustness analysis.

## License

Open access for academic and research use. Please cite the associated article if you use or modify the materials.

## Usage

This Python script implements a fuzzy decision tree (FDT) to assist in selecting the optimal nanopore geometry based on three input criteria: charge sensitivity, size sensitivity, and trajectory impact. The model uses predefined fuzzy membership functions and a set of five decision rules to infer the most suitable geometry (conical, cigar-shaped, or hourglass) for a given sensing priority. Users can input custom values (ranging from 0 to 10) for each criterion by modifying the geometry_simulation.input variables in the script. After computation, the model outputs the recommended geometry along with a fuzzy score and provides a visual representation of the inference result.

## Simulation Models

The COMSOL simulation models were uploaded to accompany this study, providing validated computational setups for nanopore translocation simulations. These models allow users to systematically explore how pore geometry, particle size, particle charge, applied voltage, pressure differential, pore surface charge, pore dimensions, and electrolyte concentration influence the sensing response. By adjusting these parameters, users can generate application-specific simulation data to inform the fuzzy decision tree (FDT) framework for geometry selection. This integration enables tailored pore geometry recommendations based on prioritized sensing objectives, without requiring experimental trials at the initial design stage. The availability of validated simulation models ensures reproducibility and facilitates adaptation of the method to different analytical contexts.





