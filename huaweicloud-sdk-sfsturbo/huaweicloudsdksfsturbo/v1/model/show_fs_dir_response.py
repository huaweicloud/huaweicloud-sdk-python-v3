# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFsDirResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'mode': 'int',
        'uid': 'int',
        'gid': 'int'
    }

    attribute_map = {
        'path': 'path',
        'mode': 'mode',
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, path=None, mode=None, uid=None, gid=None):
        """ShowFsDirResponse

        The model defined in huaweicloud sdk

        :param path: 目录全路径
        :type path: str
        :param mode: 目录权限
        :type mode: int
        :param uid: 用户id
        :type uid: int
        :param gid: 用户组id
        :type gid: int
        """
        
        super(ShowFsDirResponse, self).__init__()

        self._path = None
        self._mode = None
        self._uid = None
        self._gid = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if mode is not None:
            self.mode = mode
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid

    @property
    def path(self):
        """Gets the path of this ShowFsDirResponse.

        目录全路径

        :return: The path of this ShowFsDirResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowFsDirResponse.

        目录全路径

        :param path: The path of this ShowFsDirResponse.
        :type path: str
        """
        self._path = path

    @property
    def mode(self):
        """Gets the mode of this ShowFsDirResponse.

        目录权限

        :return: The mode of this ShowFsDirResponse.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ShowFsDirResponse.

        目录权限

        :param mode: The mode of this ShowFsDirResponse.
        :type mode: int
        """
        self._mode = mode

    @property
    def uid(self):
        """Gets the uid of this ShowFsDirResponse.

        用户id

        :return: The uid of this ShowFsDirResponse.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ShowFsDirResponse.

        用户id

        :param uid: The uid of this ShowFsDirResponse.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this ShowFsDirResponse.

        用户组id

        :return: The gid of this ShowFsDirResponse.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ShowFsDirResponse.

        用户组id

        :param gid: The gid of this ShowFsDirResponse.
        :type gid: int
        """
        self._gid = gid

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
        if not isinstance(other, ShowFsDirResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
