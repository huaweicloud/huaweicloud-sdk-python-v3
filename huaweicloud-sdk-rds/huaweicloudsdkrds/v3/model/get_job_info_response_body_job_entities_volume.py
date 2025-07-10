# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetJobInfoResponseBodyJobEntitiesVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'original_size': 'str',
        'target_size': 'str'
    }

    attribute_map = {
        'type': 'type',
        'original_size': 'original_size',
        'target_size': 'target_size'
    }

    def __init__(self, type=None, original_size=None, target_size=None):
        r"""GetJobInfoResponseBodyJobEntitiesVolume

        The model defined in huaweicloud sdk

        :param type: 磁盘类型。
        :type type: str
        :param original_size: 实例原本的磁盘大小（单位：GB）。
        :type original_size: str
        :param target_size: 任务的目标磁盘大小（单位：GB）。
        :type target_size: str
        """
        
        

        self._type = None
        self._original_size = None
        self._target_size = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if original_size is not None:
            self.original_size = original_size
        if target_size is not None:
            self.target_size = target_size

    @property
    def type(self):
        r"""Gets the type of this GetJobInfoResponseBodyJobEntitiesVolume.

        磁盘类型。

        :return: The type of this GetJobInfoResponseBodyJobEntitiesVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GetJobInfoResponseBodyJobEntitiesVolume.

        磁盘类型。

        :param type: The type of this GetJobInfoResponseBodyJobEntitiesVolume.
        :type type: str
        """
        self._type = type

    @property
    def original_size(self):
        r"""Gets the original_size of this GetJobInfoResponseBodyJobEntitiesVolume.

        实例原本的磁盘大小（单位：GB）。

        :return: The original_size of this GetJobInfoResponseBodyJobEntitiesVolume.
        :rtype: str
        """
        return self._original_size

    @original_size.setter
    def original_size(self, original_size):
        r"""Sets the original_size of this GetJobInfoResponseBodyJobEntitiesVolume.

        实例原本的磁盘大小（单位：GB）。

        :param original_size: The original_size of this GetJobInfoResponseBodyJobEntitiesVolume.
        :type original_size: str
        """
        self._original_size = original_size

    @property
    def target_size(self):
        r"""Gets the target_size of this GetJobInfoResponseBodyJobEntitiesVolume.

        任务的目标磁盘大小（单位：GB）。

        :return: The target_size of this GetJobInfoResponseBodyJobEntitiesVolume.
        :rtype: str
        """
        return self._target_size

    @target_size.setter
    def target_size(self, target_size):
        r"""Sets the target_size of this GetJobInfoResponseBodyJobEntitiesVolume.

        任务的目标磁盘大小（单位：GB）。

        :param target_size: The target_size of this GetJobInfoResponseBodyJobEntitiesVolume.
        :type target_size: str
        """
        self._target_size = target_size

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
        if not isinstance(other, GetJobInfoResponseBodyJobEntitiesVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
