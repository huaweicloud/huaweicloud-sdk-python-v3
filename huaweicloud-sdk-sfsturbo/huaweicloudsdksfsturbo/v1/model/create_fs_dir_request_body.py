# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFsDirRequestBody:

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
        r"""CreateFsDirRequestBody

        The model defined in huaweicloud sdk

        :param path: 合法的的目录全路径
        :type path: str
        :param mode: 目录权限，默认值是755，取值范围是0到777。第一位表示目录所有者的权限，取值范围是0到7；第二位表示目录所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。目录所有者由uid指定，目录所属用户组由gid指定，不是目录所有者且不在目录所属用户组的用户为其他用户。例如：755中第一位7代表该目录所有者对该目录具有读、写、执行权限；第二位5代表该目录所属用户组对该目录具有读、执行权限；第三位5代表其他用户对该目录具有读、执行权限。
        :type mode: int
        :param uid: 目录所有者的用户id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。
        :type uid: int
        :param gid: 目录所属用户组id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。
        :type gid: int
        """
        
        

        self._path = None
        self._mode = None
        self._uid = None
        self._gid = None
        self.discriminator = None

        self.path = path
        if mode is not None:
            self.mode = mode
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid

    @property
    def path(self):
        r"""Gets the path of this CreateFsDirRequestBody.

        合法的的目录全路径

        :return: The path of this CreateFsDirRequestBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CreateFsDirRequestBody.

        合法的的目录全路径

        :param path: The path of this CreateFsDirRequestBody.
        :type path: str
        """
        self._path = path

    @property
    def mode(self):
        r"""Gets the mode of this CreateFsDirRequestBody.

        目录权限，默认值是755，取值范围是0到777。第一位表示目录所有者的权限，取值范围是0到7；第二位表示目录所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。目录所有者由uid指定，目录所属用户组由gid指定，不是目录所有者且不在目录所属用户组的用户为其他用户。例如：755中第一位7代表该目录所有者对该目录具有读、写、执行权限；第二位5代表该目录所属用户组对该目录具有读、执行权限；第三位5代表其他用户对该目录具有读、执行权限。

        :return: The mode of this CreateFsDirRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateFsDirRequestBody.

        目录权限，默认值是755，取值范围是0到777。第一位表示目录所有者的权限，取值范围是0到7；第二位表示目录所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。目录所有者由uid指定，目录所属用户组由gid指定，不是目录所有者且不在目录所属用户组的用户为其他用户。例如：755中第一位7代表该目录所有者对该目录具有读、写、执行权限；第二位5代表该目录所属用户组对该目录具有读、执行权限；第三位5代表其他用户对该目录具有读、执行权限。

        :param mode: The mode of this CreateFsDirRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def uid(self):
        r"""Gets the uid of this CreateFsDirRequestBody.

        目录所有者的用户id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :return: The uid of this CreateFsDirRequestBody.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this CreateFsDirRequestBody.

        目录所有者的用户id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :param uid: The uid of this CreateFsDirRequestBody.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this CreateFsDirRequestBody.

        目录所属用户组id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :return: The gid of this CreateFsDirRequestBody.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this CreateFsDirRequestBody.

        目录所属用户组id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :param gid: The gid of this CreateFsDirRequestBody.
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
        if not isinstance(other, CreateFsDirRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
