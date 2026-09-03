# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_interval': 'int',
        'sub_task_name': 'str'
    }

    attribute_map = {
        'collect_interval': 'collect_interval',
        'sub_task_name': 'sub_task_name'
    }

    def __init__(self, collect_interval=None, sub_task_name=None):
        r"""BasicInfoVo

        The model defined in huaweicloud sdk

        :param collect_interval: 采集间隔以秒为单位
        :type collect_interval: int
        :param sub_task_name: 子任务名称
        :type sub_task_name: str
        """
        
        

        self._collect_interval = None
        self._sub_task_name = None
        self.discriminator = None

        if collect_interval is not None:
            self.collect_interval = collect_interval
        if sub_task_name is not None:
            self.sub_task_name = sub_task_name

    @property
    def collect_interval(self):
        r"""Gets the collect_interval of this BasicInfoVo.

        采集间隔以秒为单位

        :return: The collect_interval of this BasicInfoVo.
        :rtype: int
        """
        return self._collect_interval

    @collect_interval.setter
    def collect_interval(self, collect_interval):
        r"""Sets the collect_interval of this BasicInfoVo.

        采集间隔以秒为单位

        :param collect_interval: The collect_interval of this BasicInfoVo.
        :type collect_interval: int
        """
        self._collect_interval = collect_interval

    @property
    def sub_task_name(self):
        r"""Gets the sub_task_name of this BasicInfoVo.

        子任务名称

        :return: The sub_task_name of this BasicInfoVo.
        :rtype: str
        """
        return self._sub_task_name

    @sub_task_name.setter
    def sub_task_name(self, sub_task_name):
        r"""Sets the sub_task_name of this BasicInfoVo.

        子任务名称

        :param sub_task_name: The sub_task_name of this BasicInfoVo.
        :type sub_task_name: str
        """
        self._sub_task_name = sub_task_name

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
        if not isinstance(other, BasicInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
