.. include:: ../links.inc

The Data Object
===============

Description
^^^^^^^^^^^

This is the *object* that traverses the steps of the pipeline. It is indeed a
dictionary of dictionaries. The first level of keys are the :ref:`data_types`
and a special key named ``meta`` that contains all the information on the data
object including source and previous transformation steps.

The second level of keys are the actual data. So far, there are two keys used:

- ``path``: path to the file containing the data.
- ``data``: the data loaded in memory.

The :ref:`datagrabber` step will only fill the ``path`` value.
The ``data`` value will be filled by the :ref:`datareader` step, if it is one of the possible file types
that the datareader can read.

.. _data_types:

Data types
^^^^^^^^^^

.. list-table:: Built-in data types
   :widths: 30 80 40
   :header-rows: 1

   * - Name
     - Description
     - Example
   * - ``T1w``
     - T1w image (3D)
     - Preprocessed or Raw T1w image
   * - ``BOLD``
     - BOLD image (4D)
     - Preprocessed/Denoised BOLD image (fmriprep output)
   * - ``VBM_GM``
     - VBM Gray Matter segmentation (3D)
     - CAT output (`m0wp1` images)
   * - ``VBM_WM``
     - VBM White Matter segmentation (3D)
     - CAT output (`m0wp2` images)
