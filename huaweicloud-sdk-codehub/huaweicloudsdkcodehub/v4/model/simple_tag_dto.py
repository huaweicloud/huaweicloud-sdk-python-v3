# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleTagDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'message': 'str',
        'target': 'str',
        'gpg_key': 'GpgKeyDto',
        'can_delete': 'bool',
        'can_read': 'bool',
        'can_download': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'message': 'message',
        'target': 'target',
        'gpg_key': 'gpgKey',
        'can_delete': 'can_delete',
        'can_read': 'can_read',
        'can_download': 'can_download'
    }

    def __init__(self, name=None, message=None, target=None, gpg_key=None, can_delete=None, can_read=None, can_download=None):
        r"""SimpleTagDto

        The model defined in huaweicloud sdk

        :param name: 标签名称
        :type name: str
        :param message: 标签描述
        :type message: str
        :param target: 目标commit_id
        :type target: str
        :param gpg_key: 
        :type gpg_key: :class:`huaweicloudsdkcodehub.v4.GpgKeyDto`
        :param can_delete: 是否可以被删除
        :type can_delete: bool
        :param can_read: 是否可以被查看
        :type can_read: bool
        :param can_download: 是否可以被下载
        :type can_download: bool
        """
        
        

        self._name = None
        self._message = None
        self._target = None
        self._gpg_key = None
        self._can_delete = None
        self._can_read = None
        self._can_download = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if target is not None:
            self.target = target
        if gpg_key is not None:
            self.gpg_key = gpg_key
        if can_delete is not None:
            self.can_delete = can_delete
        if can_read is not None:
            self.can_read = can_read
        if can_download is not None:
            self.can_download = can_download

    @property
    def name(self):
        r"""Gets the name of this SimpleTagDto.

        标签名称

        :return: The name of this SimpleTagDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SimpleTagDto.

        标签名称

        :param name: The name of this SimpleTagDto.
        :type name: str
        """
        self._name = name

    @property
    def message(self):
        r"""Gets the message of this SimpleTagDto.

        标签描述

        :return: The message of this SimpleTagDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SimpleTagDto.

        标签描述

        :param message: The message of this SimpleTagDto.
        :type message: str
        """
        self._message = message

    @property
    def target(self):
        r"""Gets the target of this SimpleTagDto.

        目标commit_id

        :return: The target of this SimpleTagDto.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this SimpleTagDto.

        目标commit_id

        :param target: The target of this SimpleTagDto.
        :type target: str
        """
        self._target = target

    @property
    def gpg_key(self):
        r"""Gets the gpg_key of this SimpleTagDto.

        :return: The gpg_key of this SimpleTagDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.GpgKeyDto`
        """
        return self._gpg_key

    @gpg_key.setter
    def gpg_key(self, gpg_key):
        r"""Sets the gpg_key of this SimpleTagDto.

        :param gpg_key: The gpg_key of this SimpleTagDto.
        :type gpg_key: :class:`huaweicloudsdkcodehub.v4.GpgKeyDto`
        """
        self._gpg_key = gpg_key

    @property
    def can_delete(self):
        r"""Gets the can_delete of this SimpleTagDto.

        是否可以被删除

        :return: The can_delete of this SimpleTagDto.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this SimpleTagDto.

        是否可以被删除

        :param can_delete: The can_delete of this SimpleTagDto.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_read(self):
        r"""Gets the can_read of this SimpleTagDto.

        是否可以被查看

        :return: The can_read of this SimpleTagDto.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        r"""Sets the can_read of this SimpleTagDto.

        是否可以被查看

        :param can_read: The can_read of this SimpleTagDto.
        :type can_read: bool
        """
        self._can_read = can_read

    @property
    def can_download(self):
        r"""Gets the can_download of this SimpleTagDto.

        是否可以被下载

        :return: The can_download of this SimpleTagDto.
        :rtype: bool
        """
        return self._can_download

    @can_download.setter
    def can_download(self, can_download):
        r"""Sets the can_download of this SimpleTagDto.

        是否可以被下载

        :param can_download: The can_download of this SimpleTagDto.
        :type can_download: bool
        """
        self._can_download = can_download

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
        if not isinstance(other, SimpleTagDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
