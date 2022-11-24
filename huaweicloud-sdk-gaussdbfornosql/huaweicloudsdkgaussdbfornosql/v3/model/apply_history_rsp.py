# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyHistoryRsp:

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
        'applied_at': 'datetime',
        'apply_result': 'str',
        'failure_reason': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'applied_at': 'applied_at',
        'apply_result': 'apply_result',
        'failure_reason': 'failure_reason'
    }

    def __init__(self, instance_id=None, instance_name=None, applied_at=None, apply_result=None, failure_reason=None):
        """ApplyHistoryRsp

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param applied_at: 生效时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。  [其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。](tag:hc)  [其中，T指某个时间的开始；Z指时区偏移量。](tag:hk)
        :type applied_at: datetime
        :param apply_result: - SUCCESS：应用成功。 - FAILED:应用失败。
        :type apply_result: str
        :param failure_reason: 失败原因
        :type failure_reason: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._applied_at = None
        self._apply_result = None
        self._failure_reason = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.applied_at = applied_at
        self.apply_result = apply_result
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def instance_id(self):
        """Gets the instance_id of this ApplyHistoryRsp.

        实例ID。

        :return: The instance_id of this ApplyHistoryRsp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ApplyHistoryRsp.

        实例ID。

        :param instance_id: The instance_id of this ApplyHistoryRsp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ApplyHistoryRsp.

        实例名称

        :return: The instance_name of this ApplyHistoryRsp.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ApplyHistoryRsp.

        实例名称

        :param instance_name: The instance_name of this ApplyHistoryRsp.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def applied_at(self):
        """Gets the applied_at of this ApplyHistoryRsp.

        生效时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  [其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。](tag:hc)  [其中，T指某个时间的开始；Z指时区偏移量。](tag:hk)

        :return: The applied_at of this ApplyHistoryRsp.
        :rtype: datetime
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        """Sets the applied_at of this ApplyHistoryRsp.

        生效时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。  [其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。](tag:hc)  [其中，T指某个时间的开始；Z指时区偏移量。](tag:hk)

        :param applied_at: The applied_at of this ApplyHistoryRsp.
        :type applied_at: datetime
        """
        self._applied_at = applied_at

    @property
    def apply_result(self):
        """Gets the apply_result of this ApplyHistoryRsp.

        - SUCCESS：应用成功。 - FAILED:应用失败。

        :return: The apply_result of this ApplyHistoryRsp.
        :rtype: str
        """
        return self._apply_result

    @apply_result.setter
    def apply_result(self, apply_result):
        """Sets the apply_result of this ApplyHistoryRsp.

        - SUCCESS：应用成功。 - FAILED:应用失败。

        :param apply_result: The apply_result of this ApplyHistoryRsp.
        :type apply_result: str
        """
        self._apply_result = apply_result

    @property
    def failure_reason(self):
        """Gets the failure_reason of this ApplyHistoryRsp.

        失败原因

        :return: The failure_reason of this ApplyHistoryRsp.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this ApplyHistoryRsp.

        失败原因

        :param failure_reason: The failure_reason of this ApplyHistoryRsp.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

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
        if not isinstance(other, ApplyHistoryRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
