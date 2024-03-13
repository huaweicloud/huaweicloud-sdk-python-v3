# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDEPrivilageProjectInfo:

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
        'ids': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'ids': 'ids'
    }

    def __init__(self, project_id=None, ids=None):
        """IDEPrivilageProjectInfo

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param ids: tab_id集合
        :type ids: list[str]
        """
        
        

        self._project_id = None
        self._ids = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if ids is not None:
            self.ids = ids

    @property
    def project_id(self):
        """Gets the project_id of this IDEPrivilageProjectInfo.

        项目id

        :return: The project_id of this IDEPrivilageProjectInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IDEPrivilageProjectInfo.

        项目id

        :param project_id: The project_id of this IDEPrivilageProjectInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ids(self):
        """Gets the ids of this IDEPrivilageProjectInfo.

        tab_id集合

        :return: The ids of this IDEPrivilageProjectInfo.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this IDEPrivilageProjectInfo.

        tab_id集合

        :param ids: The ids of this IDEPrivilageProjectInfo.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, IDEPrivilageProjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
