# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBasicAwRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'aw_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'aw_id': 'aw_id'
    }

    def __init__(self, project_id=None, aw_id=None):
        """ListBasicAwRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param aw_id: AW ID
        :type aw_id: str
        """
        
        

        self._project_id = None
        self._aw_id = None
        self.discriminator = None

        self.project_id = project_id
        self.aw_id = aw_id

    @property
    def project_id(self):
        """Gets the project_id of this ListBasicAwRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListBasicAwRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListBasicAwRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListBasicAwRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def aw_id(self):
        """Gets the aw_id of this ListBasicAwRequest.

        AW ID

        :return: The aw_id of this ListBasicAwRequest.
        :rtype: str
        """
        return self._aw_id

    @aw_id.setter
    def aw_id(self, aw_id):
        """Sets the aw_id of this ListBasicAwRequest.

        AW ID

        :param aw_id: The aw_id of this ListBasicAwRequest.
        :type aw_id: str
        """
        self._aw_id = aw_id

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
        if not isinstance(other, ListBasicAwRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
