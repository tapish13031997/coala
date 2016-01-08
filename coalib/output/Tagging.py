import hashlib
import pickle
import os

from coalib.misc import Constants


def get_tag_path(tag, project):
    """
    Creates a hash value that is used for tagging and creates a path for it.

    :param tag:     The name for the tag.
    :param project: The related coafile.
    :return:        A path containing a hash as filename that identifies the
                    given parameters.
    """
    path = os.path.join(project, tag)
    hash = hashlib.sha224(path.encode()).hexdigest()
    return os.path.join(Constants.TAGS_DIR, hash)


def tag_results(tag, project, results):
    """
    This method takes a tag provided from the user and saves the results
    dictionary output by coala to a file. That file is uniquely identified by
    the combined hash of the project (i.e. coafile) and the provided tag.

    :param tag:     Tag provided by user.
    :param project: Path to the coafile the results belong to.
    :param results: Results dictionary generated by coala.
    """
    with open(get_tag_path(tag, project), 'wb+') as file:
        pickle.dump(results, file)


def load_tagged_results(tag, project):
    """
    Retrieves results previously stored with tag_results.

    :param tag:     The tag name.
    :param project: Path to the coafile the results belong to.
    :return:        A results dictionary, as generated by coala.
    """
    with open(get_tag_path(tag, project), 'rb') as file:
        return pickle.load(file)


def delete_tagged_results(tag, project):
    """
    Deletes previously tagged results.

    :param tag:     The tag name.
    :param project: Path to the coafile the results belong to.
    """
    file_path = get_tag_path(tag, project)
    if os.path.exists(file_path):
        os.remove(file_path)
