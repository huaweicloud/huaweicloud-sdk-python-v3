# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildRecordBuildRecordType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rerun': 'bool',
        'trigger_type': 'str',
        'record_type': 'str',
        'is_rerun': 'bool'
    }

    attribute_map = {
        'rerun': 'rerun',
        'trigger_type': 'trigger_type',
        'record_type': 'record_type',
        'is_rerun': 'is_rerun'
    }

    def __init__(self, rerun=None, trigger_type=None, record_type=None, is_rerun=None):
        r"""BuildRecordBuildRecordType

        The model defined in huaweicloud sdk

        :param rerun: 是否rerun
        :type rerun: bool
        :param trigger_type: 触发类型
        :type trigger_type: str
        :param record_type: 记录类型
        :type record_type: str
        :param is_rerun: 是否返回
        :type is_rerun: bool
        """
        
        

        self._rerun = None
        self._trigger_type = None
        self._record_type = None
        self._is_rerun = None
        self.discriminator = None

        if rerun is not None:
            self.rerun = rerun
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if record_type is not None:
            self.record_type = record_type
        if is_rerun is not None:
            self.is_rerun = is_rerun

    @property
    def rerun(self):
        r"""Gets the rerun of this BuildRecordBuildRecordType.

        是否rerun

        :return: The rerun of this BuildRecordBuildRecordType.
        :rtype: bool
        """
        return self._rerun

    @rerun.setter
    def rerun(self, rerun):
        r"""Sets the rerun of this BuildRecordBuildRecordType.

        是否rerun

        :param rerun: The rerun of this BuildRecordBuildRecordType.
        :type rerun: bool
        """
        self._rerun = rerun

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this BuildRecordBuildRecordType.

        触发类型

        :return: The trigger_type of this BuildRecordBuildRecordType.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this BuildRecordBuildRecordType.

        触发类型

        :param trigger_type: The trigger_type of this BuildRecordBuildRecordType.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def record_type(self):
        r"""Gets the record_type of this BuildRecordBuildRecordType.

        记录类型

        :return: The record_type of this BuildRecordBuildRecordType.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        r"""Sets the record_type of this BuildRecordBuildRecordType.

        记录类型

        :param record_type: The record_type of this BuildRecordBuildRecordType.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def is_rerun(self):
        r"""Gets the is_rerun of this BuildRecordBuildRecordType.

        是否返回

        :return: The is_rerun of this BuildRecordBuildRecordType.
        :rtype: bool
        """
        return self._is_rerun

    @is_rerun.setter
    def is_rerun(self, is_rerun):
        r"""Sets the is_rerun of this BuildRecordBuildRecordType.

        是否返回

        :param is_rerun: The is_rerun of this BuildRecordBuildRecordType.
        :type is_rerun: bool
        """
        self._is_rerun = is_rerun

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
        if not isinstance(other, BuildRecordBuildRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
