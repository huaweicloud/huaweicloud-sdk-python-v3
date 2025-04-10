# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserQosReqInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pid': 'str',
        'access_media_type': 'str'
    }

    attribute_map = {
        'pid': 'pid',
        'access_media_type': 'accessMediaType'
    }

    def __init__(self, pid=None, access_media_type=None):
        r"""UserQosReqInfo

        The model defined in huaweicloud sdk

        :param pid: 用户pid
        :type pid: str
        :param access_media_type: 用户接入媒体类型
        :type access_media_type: str
        """
        
        

        self._pid = None
        self._access_media_type = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if access_media_type is not None:
            self.access_media_type = access_media_type

    @property
    def pid(self):
        r"""Gets the pid of this UserQosReqInfo.

        用户pid

        :return: The pid of this UserQosReqInfo.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this UserQosReqInfo.

        用户pid

        :param pid: The pid of this UserQosReqInfo.
        :type pid: str
        """
        self._pid = pid

    @property
    def access_media_type(self):
        r"""Gets the access_media_type of this UserQosReqInfo.

        用户接入媒体类型

        :return: The access_media_type of this UserQosReqInfo.
        :rtype: str
        """
        return self._access_media_type

    @access_media_type.setter
    def access_media_type(self, access_media_type):
        r"""Sets the access_media_type of this UserQosReqInfo.

        用户接入媒体类型

        :param access_media_type: The access_media_type of this UserQosReqInfo.
        :type access_media_type: str
        """
        self._access_media_type = access_media_type

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
        if not isinstance(other, UserQosReqInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
