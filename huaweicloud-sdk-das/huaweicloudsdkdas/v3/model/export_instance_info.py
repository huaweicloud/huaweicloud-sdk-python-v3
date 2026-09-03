# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportInstanceInfo:

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
        'instance_name': 'str',
        'instance_status': 'str',
        'metrics': 'dict(str, float)'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'metrics': 'metrics'
    }

    def __init__(self, instance_id=None, instance_name=None, instance_status=None, metrics=None):
        r"""ExportInstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param instance_status: 实例状态
        :type instance_status: str
        :param metrics: 指标信息
        :type metrics: dict(str, float)
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._metrics = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if metrics is not None:
            self.metrics = metrics

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExportInstanceInfo.

        实例ID

        :return: The instance_id of this ExportInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExportInstanceInfo.

        实例ID

        :param instance_id: The instance_id of this ExportInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ExportInstanceInfo.

        实例名称

        :return: The instance_name of this ExportInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ExportInstanceInfo.

        实例名称

        :param instance_name: The instance_name of this ExportInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ExportInstanceInfo.

        实例状态

        :return: The instance_status of this ExportInstanceInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ExportInstanceInfo.

        实例状态

        :param instance_status: The instance_status of this ExportInstanceInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def metrics(self):
        r"""Gets the metrics of this ExportInstanceInfo.

        指标信息

        :return: The metrics of this ExportInstanceInfo.
        :rtype: dict(str, float)
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ExportInstanceInfo.

        指标信息

        :param metrics: The metrics of this ExportInstanceInfo.
        :type metrics: dict(str, float)
        """
        self._metrics = metrics

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
        if not isinstance(other, ExportInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
