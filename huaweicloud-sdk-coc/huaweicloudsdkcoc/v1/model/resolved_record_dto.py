# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResolvedRecordDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolved_time': 'int',
        'create_name': 'str',
        'remarks': 'str'
    }

    attribute_map = {
        'resolved_time': 'resolved_time',
        'create_name': 'create_name',
        'remarks': 'remarks'
    }

    def __init__(self, resolved_time=None, create_name=None, remarks=None):
        r"""ResolvedRecordDTO

        The model defined in huaweicloud sdk

        :param resolved_time: 清除汇聚告警的时间
        :type resolved_time: int
        :param create_name: 执行人
        :type create_name: str
        :param remarks: 清除时填写的备注
        :type remarks: str
        """
        
        

        self._resolved_time = None
        self._create_name = None
        self._remarks = None
        self.discriminator = None

        if resolved_time is not None:
            self.resolved_time = resolved_time
        if create_name is not None:
            self.create_name = create_name
        if remarks is not None:
            self.remarks = remarks

    @property
    def resolved_time(self):
        r"""Gets the resolved_time of this ResolvedRecordDTO.

        清除汇聚告警的时间

        :return: The resolved_time of this ResolvedRecordDTO.
        :rtype: int
        """
        return self._resolved_time

    @resolved_time.setter
    def resolved_time(self, resolved_time):
        r"""Sets the resolved_time of this ResolvedRecordDTO.

        清除汇聚告警的时间

        :param resolved_time: The resolved_time of this ResolvedRecordDTO.
        :type resolved_time: int
        """
        self._resolved_time = resolved_time

    @property
    def create_name(self):
        r"""Gets the create_name of this ResolvedRecordDTO.

        执行人

        :return: The create_name of this ResolvedRecordDTO.
        :rtype: str
        """
        return self._create_name

    @create_name.setter
    def create_name(self, create_name):
        r"""Sets the create_name of this ResolvedRecordDTO.

        执行人

        :param create_name: The create_name of this ResolvedRecordDTO.
        :type create_name: str
        """
        self._create_name = create_name

    @property
    def remarks(self):
        r"""Gets the remarks of this ResolvedRecordDTO.

        清除时填写的备注

        :return: The remarks of this ResolvedRecordDTO.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this ResolvedRecordDTO.

        清除时填写的备注

        :param remarks: The remarks of this ResolvedRecordDTO.
        :type remarks: str
        """
        self._remarks = remarks

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
        if not isinstance(other, ResolvedRecordDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
