#  Using Machine Learning for Move Sequence Visualization and Generation in Climbing

This project explores the application of Machine Learning techniques to sport climbing, as part of the Semester Project at EPFL, under the supervision of Martin Jaggi. Expanding upon previous projects, we develop a visualization tool for move sequence evaluation on a given boulder. Then, we look into move sequence prediction from simple holds sequence information using three different Transformer models. While the results are not conclusive, they are a first step in this kind of approach and lay the ground for future work.

## Repository Structure
- The `Documentation` folder contains the report and presentation of this project, as well as references for previous works on this subject.
- The `Data` folder contains all the necessary datasets used in this project. In particular, the `Documentation/moonboard` folder contains the moonboard data used for visualization and is where the output is stored.
- The `Prediction` folder contains the notebooks used to experiment with move sequence prediction/generation from the holds sequence. Several different implementations have been looked at, with various degrees of success.
- The `Selection_Visualization` folder contains the whole pipeline for Move Sequence selection on the Moonboard, as well as the visualization of this sequence with a generated skeleton