# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDataJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_job_id': 'str',
        'eihealth_project_id': 'str'
    }

    attribute_map = {
        'data_job_id': 'data_job_id',
        'eihealth_project_id': 'eihealth_project_id'
    }

    def __init__(self, data_job_id=None, eihealth_project_id=None):
        """DeleteDataJobRequest

        The model defined in huaweicloud sdk

        :param data_job_id: 数据作业id
        :type data_job_id: str
        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        """
        
        

        self._data_job_id = None
        self._eihealth_project_id = None
        self.discriminator = None

        self.data_job_id = data_job_id
        self.eihealth_project_id = eihealth_project_id

    @property
    def data_job_id(self):
        """Gets the data_job_id of this DeleteDataJobRequest.

        数据作业id

        :return: The data_job_id of this DeleteDataJobRequest.
        :rtype: str
        """
        return self._data_job_id

    @data_job_id.setter
    def data_job_id(self, data_job_id):
        """Sets the data_job_id of this DeleteDataJobRequest.

        数据作业id

        :param data_job_id: The data_job_id of this DeleteDataJobRequest.
        :type data_job_id: str
        """
        self._data_job_id = data_job_id

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this DeleteDataJobRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this DeleteDataJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this DeleteDataJobRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this DeleteDataJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

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
        if not isinstance(other, DeleteDataJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
