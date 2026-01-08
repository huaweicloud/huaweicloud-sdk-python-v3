# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePackage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'description': 'dict(str, str)',
        'status': 'str',
        'period_type': 'str',
        'period_value': 'int',
        'measurement_name': 'str',
        'threshold': 'int'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'description': 'description',
        'status': 'status',
        'period_type': 'period_type',
        'period_value': 'period_value',
        'measurement_name': 'measurement_name',
        'threshold': 'threshold'
    }

    def __init__(self, resource_spec_code=None, description=None, status=None, period_type=None, period_value=None, measurement_name=None, threshold=None):
        r"""ResourcePackage

        The model defined in huaweicloud sdk

        :param resource_spec_code: 资源规格编码。
        :type resource_spec_code: str
        :param description: 产品描述&lt;语言，各语言对应的产品名&gt;。
        :type description: dict(str, str)
        :param status: 产品状态，normal/onSell：正常、sellout：售空、abandon：下线。
        :type status: str
        :param period_type: 周期类型，MONTH：月。
        :type period_type: str
        :param period_value: 数量，单位:月。
        :type period_value: int
        :param measurement_name: 资源包单位，hour：小时。
        :type measurement_name: str
        :param threshold: 资源包总量。
        :type threshold: int
        """
        
        

        self._resource_spec_code = None
        self._description = None
        self._status = None
        self._period_type = None
        self._period_value = None
        self._measurement_name = None
        self._threshold = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if period_type is not None:
            self.period_type = period_type
        if period_value is not None:
            self.period_value = period_value
        if measurement_name is not None:
            self.measurement_name = measurement_name
        if threshold is not None:
            self.threshold = threshold

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ResourcePackage.

        资源规格编码。

        :return: The resource_spec_code of this ResourcePackage.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ResourcePackage.

        资源规格编码。

        :param resource_spec_code: The resource_spec_code of this ResourcePackage.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def description(self):
        r"""Gets the description of this ResourcePackage.

        产品描述<语言，各语言对应的产品名>。

        :return: The description of this ResourcePackage.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ResourcePackage.

        产品描述<语言，各语言对应的产品名>。

        :param description: The description of this ResourcePackage.
        :type description: dict(str, str)
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ResourcePackage.

        产品状态，normal/onSell：正常、sellout：售空、abandon：下线。

        :return: The status of this ResourcePackage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourcePackage.

        产品状态，normal/onSell：正常、sellout：售空、abandon：下线。

        :param status: The status of this ResourcePackage.
        :type status: str
        """
        self._status = status

    @property
    def period_type(self):
        r"""Gets the period_type of this ResourcePackage.

        周期类型，MONTH：月。

        :return: The period_type of this ResourcePackage.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ResourcePackage.

        周期类型，MONTH：月。

        :param period_type: The period_type of this ResourcePackage.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_value(self):
        r"""Gets the period_value of this ResourcePackage.

        数量，单位:月。

        :return: The period_value of this ResourcePackage.
        :rtype: int
        """
        return self._period_value

    @period_value.setter
    def period_value(self, period_value):
        r"""Sets the period_value of this ResourcePackage.

        数量，单位:月。

        :param period_value: The period_value of this ResourcePackage.
        :type period_value: int
        """
        self._period_value = period_value

    @property
    def measurement_name(self):
        r"""Gets the measurement_name of this ResourcePackage.

        资源包单位，hour：小时。

        :return: The measurement_name of this ResourcePackage.
        :rtype: str
        """
        return self._measurement_name

    @measurement_name.setter
    def measurement_name(self, measurement_name):
        r"""Sets the measurement_name of this ResourcePackage.

        资源包单位，hour：小时。

        :param measurement_name: The measurement_name of this ResourcePackage.
        :type measurement_name: str
        """
        self._measurement_name = measurement_name

    @property
    def threshold(self):
        r"""Gets the threshold of this ResourcePackage.

        资源包总量。

        :return: The threshold of this ResourcePackage.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ResourcePackage.

        资源包总量。

        :param threshold: The threshold of this ResourcePackage.
        :type threshold: int
        """
        self._threshold = threshold

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourcePackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
