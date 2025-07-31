# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveBrowsingHistoryRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'path': 'str',
        'id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'path': 'path',
        'id': 'id'
    }

    def __init__(self, action=None, path=None, id=None):
        r"""SaveBrowsingHistoryRequestInfo

        The model defined in huaweicloud sdk

        :param action: 用户页面访问动作in:进入页面，out:离开页面
        :type action: str
        :param path: 路径
        :type path: str
        :param id: 访问记录id,仅当type为out时携带
        :type id: str
        """
        
        

        self._action = None
        self._path = None
        self._id = None
        self.discriminator = None

        self.action = action
        self.path = path
        if id is not None:
            self.id = id

    @property
    def action(self):
        r"""Gets the action of this SaveBrowsingHistoryRequestInfo.

        用户页面访问动作in:进入页面，out:离开页面

        :return: The action of this SaveBrowsingHistoryRequestInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this SaveBrowsingHistoryRequestInfo.

        用户页面访问动作in:进入页面，out:离开页面

        :param action: The action of this SaveBrowsingHistoryRequestInfo.
        :type action: str
        """
        self._action = action

    @property
    def path(self):
        r"""Gets the path of this SaveBrowsingHistoryRequestInfo.

        路径

        :return: The path of this SaveBrowsingHistoryRequestInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SaveBrowsingHistoryRequestInfo.

        路径

        :param path: The path of this SaveBrowsingHistoryRequestInfo.
        :type path: str
        """
        self._path = path

    @property
    def id(self):
        r"""Gets the id of this SaveBrowsingHistoryRequestInfo.

        访问记录id,仅当type为out时携带

        :return: The id of this SaveBrowsingHistoryRequestInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SaveBrowsingHistoryRequestInfo.

        访问记录id,仅当type为out时携带

        :param id: The id of this SaveBrowsingHistoryRequestInfo.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, SaveBrowsingHistoryRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
