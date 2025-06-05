# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SfsTurboRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'space': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'space': 'space'
    }

    def __init__(self, id=None, name=None, status=None, type=None, space=None):
        r"""SfsTurboRsp

        The model defined in huaweicloud sdk

        :param id: sfs-turbo资源ID。
        :type id: str
        :param name: sfs-turbo资源名称。
        :type name: str
        :param status: sfs-turbo资源状态。
        :type status: str
        :param type: sfs-turbo资源类型。
        :type type: str
        :param space: sfs-turbo资源容量，单位GB。
        :type space: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self._space = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if space is not None:
            self.space = space

    @property
    def id(self):
        r"""Gets the id of this SfsTurboRsp.

        sfs-turbo资源ID。

        :return: The id of this SfsTurboRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SfsTurboRsp.

        sfs-turbo资源ID。

        :param id: The id of this SfsTurboRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SfsTurboRsp.

        sfs-turbo资源名称。

        :return: The name of this SfsTurboRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SfsTurboRsp.

        sfs-turbo资源名称。

        :param name: The name of this SfsTurboRsp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this SfsTurboRsp.

        sfs-turbo资源状态。

        :return: The status of this SfsTurboRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SfsTurboRsp.

        sfs-turbo资源状态。

        :param status: The status of this SfsTurboRsp.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this SfsTurboRsp.

        sfs-turbo资源类型。

        :return: The type of this SfsTurboRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SfsTurboRsp.

        sfs-turbo资源类型。

        :param type: The type of this SfsTurboRsp.
        :type type: str
        """
        self._type = type

    @property
    def space(self):
        r"""Gets the space of this SfsTurboRsp.

        sfs-turbo资源容量，单位GB。

        :return: The space of this SfsTurboRsp.
        :rtype: str
        """
        return self._space

    @space.setter
    def space(self, space):
        r"""Sets the space of this SfsTurboRsp.

        sfs-turbo资源容量，单位GB。

        :param space: The space of this SfsTurboRsp.
        :type space: str
        """
        self._space = space

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
        if not isinstance(other, SfsTurboRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
