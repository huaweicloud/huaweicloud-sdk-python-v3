# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDisasterRecoverySettingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, offset=None, limit=None):
        r"""ShowDisasterRecoverySettingsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param offset: 索引位置偏移量，表示从指定offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0。
        :type offset: int
        :param limit: 查询实例个数上限值。 取值范围：1~50。不传该参数时，默认查询前50条实例信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDisasterRecoverySettingsRequest.

        实例ID。

        :return: The instance_id of this ShowDisasterRecoverySettingsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDisasterRecoverySettingsRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowDisasterRecoverySettingsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowDisasterRecoverySettingsRequest.

        索引位置偏移量，表示从指定offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :return: The offset of this ShowDisasterRecoverySettingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDisasterRecoverySettingsRequest.

        索引位置偏移量，表示从指定offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :param offset: The offset of this ShowDisasterRecoverySettingsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDisasterRecoverySettingsRequest.

        查询实例个数上限值。 取值范围：1~50。不传该参数时，默认查询前50条实例信息。

        :return: The limit of this ShowDisasterRecoverySettingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDisasterRecoverySettingsRequest.

        查询实例个数上限值。 取值范围：1~50。不传该参数时，默认查询前50条实例信息。

        :param limit: The limit of this ShowDisasterRecoverySettingsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowDisasterRecoverySettingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
