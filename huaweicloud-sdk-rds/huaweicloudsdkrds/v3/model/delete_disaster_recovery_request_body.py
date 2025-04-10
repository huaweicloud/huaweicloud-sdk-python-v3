# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDisasterRecoveryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_instance_id': 'str',
        'target_project_id': 'str',
        'target_region': 'str',
        'target_ip': 'str',
        'is_master': 'bool'
    }

    attribute_map = {
        'target_instance_id': 'target_instance_id',
        'target_project_id': 'target_project_id',
        'target_region': 'target_region',
        'target_ip': 'target_ip',
        'is_master': 'is_master'
    }

    def __init__(self, target_instance_id=None, target_project_id=None, target_region=None, target_ip=None, is_master=None):
        r"""DeleteDisasterRecoveryRequestBody

        The model defined in huaweicloud sdk

        :param target_instance_id: 解除目标的实例id
        :type target_instance_id: str
        :param target_project_id: 解除目标的project id
        :type target_project_id: str
        :param target_region: 解除目标的region
        :type target_region: str
        :param target_ip: 解除目标的数据浮动ip
        :type target_ip: str
        :param is_master: 当前操作对象是否是主实例
        :type is_master: bool
        """
        
        

        self._target_instance_id = None
        self._target_project_id = None
        self._target_region = None
        self._target_ip = None
        self._is_master = None
        self.discriminator = None

        self.target_instance_id = target_instance_id
        self.target_project_id = target_project_id
        self.target_region = target_region
        self.target_ip = target_ip
        self.is_master = is_master

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this DeleteDisasterRecoveryRequestBody.

        解除目标的实例id

        :return: The target_instance_id of this DeleteDisasterRecoveryRequestBody.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this DeleteDisasterRecoveryRequestBody.

        解除目标的实例id

        :param target_instance_id: The target_instance_id of this DeleteDisasterRecoveryRequestBody.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this DeleteDisasterRecoveryRequestBody.

        解除目标的project id

        :return: The target_project_id of this DeleteDisasterRecoveryRequestBody.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this DeleteDisasterRecoveryRequestBody.

        解除目标的project id

        :param target_project_id: The target_project_id of this DeleteDisasterRecoveryRequestBody.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def target_region(self):
        r"""Gets the target_region of this DeleteDisasterRecoveryRequestBody.

        解除目标的region

        :return: The target_region of this DeleteDisasterRecoveryRequestBody.
        :rtype: str
        """
        return self._target_region

    @target_region.setter
    def target_region(self, target_region):
        r"""Sets the target_region of this DeleteDisasterRecoveryRequestBody.

        解除目标的region

        :param target_region: The target_region of this DeleteDisasterRecoveryRequestBody.
        :type target_region: str
        """
        self._target_region = target_region

    @property
    def target_ip(self):
        r"""Gets the target_ip of this DeleteDisasterRecoveryRequestBody.

        解除目标的数据浮动ip

        :return: The target_ip of this DeleteDisasterRecoveryRequestBody.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        r"""Sets the target_ip of this DeleteDisasterRecoveryRequestBody.

        解除目标的数据浮动ip

        :param target_ip: The target_ip of this DeleteDisasterRecoveryRequestBody.
        :type target_ip: str
        """
        self._target_ip = target_ip

    @property
    def is_master(self):
        r"""Gets the is_master of this DeleteDisasterRecoveryRequestBody.

        当前操作对象是否是主实例

        :return: The is_master of this DeleteDisasterRecoveryRequestBody.
        :rtype: bool
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        r"""Sets the is_master of this DeleteDisasterRecoveryRequestBody.

        当前操作对象是否是主实例

        :param is_master: The is_master of this DeleteDisasterRecoveryRequestBody.
        :type is_master: bool
        """
        self._is_master = is_master

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
        if not isinstance(other, DeleteDisasterRecoveryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
