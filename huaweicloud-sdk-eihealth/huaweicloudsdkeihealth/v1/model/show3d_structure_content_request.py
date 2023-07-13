# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Show3dStructureContentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'study_id': 'str',
        'job_id': 'str',
        'ligand': 'str',
        'receptor': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'study_id': 'study_id',
        'job_id': 'job_id',
        'ligand': 'ligand',
        'receptor': 'receptor'
    }

    def __init__(self, eihealth_project_id=None, study_id=None, job_id=None, ligand=None, receptor=None):
        """Show3dStructureContentRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param study_id: study_id
        :type study_id: str
        :param job_id: study作业id
        :type job_id: str
        :param ligand: 配体名称
        :type ligand: str
        :param receptor: 受体名称
        :type receptor: str
        """
        
        

        self._eihealth_project_id = None
        self._study_id = None
        self._job_id = None
        self._ligand = None
        self._receptor = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.study_id = study_id
        self.job_id = job_id
        self.ligand = ligand
        self.receptor = receptor

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this Show3dStructureContentRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this Show3dStructureContentRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this Show3dStructureContentRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this Show3dStructureContentRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def study_id(self):
        """Gets the study_id of this Show3dStructureContentRequest.

        study_id

        :return: The study_id of this Show3dStructureContentRequest.
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this Show3dStructureContentRequest.

        study_id

        :param study_id: The study_id of this Show3dStructureContentRequest.
        :type study_id: str
        """
        self._study_id = study_id

    @property
    def job_id(self):
        """Gets the job_id of this Show3dStructureContentRequest.

        study作业id

        :return: The job_id of this Show3dStructureContentRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Show3dStructureContentRequest.

        study作业id

        :param job_id: The job_id of this Show3dStructureContentRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def ligand(self):
        """Gets the ligand of this Show3dStructureContentRequest.

        配体名称

        :return: The ligand of this Show3dStructureContentRequest.
        :rtype: str
        """
        return self._ligand

    @ligand.setter
    def ligand(self, ligand):
        """Sets the ligand of this Show3dStructureContentRequest.

        配体名称

        :param ligand: The ligand of this Show3dStructureContentRequest.
        :type ligand: str
        """
        self._ligand = ligand

    @property
    def receptor(self):
        """Gets the receptor of this Show3dStructureContentRequest.

        受体名称

        :return: The receptor of this Show3dStructureContentRequest.
        :rtype: str
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        """Sets the receptor of this Show3dStructureContentRequest.

        受体名称

        :param receptor: The receptor of this Show3dStructureContentRequest.
        :type receptor: str
        """
        self._receptor = receptor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Show3dStructureContentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
