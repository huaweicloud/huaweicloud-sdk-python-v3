# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeCbhInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'description': 'str',
        'task_id': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'task_id': 'task_id',
        'order_id': 'order_id'
    }

    def __init__(self, code=None, description=None, task_id=None, order_id=None):
        r"""UpgradeCbhInstanceResponse

        The model defined in huaweicloud sdk

        :param code: 操作结果。
        :type code: int
        :param description: 描述。
        :type description: str
        :param task_id: 任务 id。
        :type task_id: str
        :param order_id: 订单 id。
        :type order_id: str
        """
        
        super(UpgradeCbhInstanceResponse, self).__init__()

        self._code = None
        self._description = None
        self._task_id = None
        self._order_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if task_id is not None:
            self.task_id = task_id
        if order_id is not None:
            self.order_id = order_id

    @property
    def code(self):
        r"""Gets the code of this UpgradeCbhInstanceResponse.

        操作结果。

        :return: The code of this UpgradeCbhInstanceResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this UpgradeCbhInstanceResponse.

        操作结果。

        :param code: The code of this UpgradeCbhInstanceResponse.
        :type code: int
        """
        self._code = code

    @property
    def description(self):
        r"""Gets the description of this UpgradeCbhInstanceResponse.

        描述。

        :return: The description of this UpgradeCbhInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpgradeCbhInstanceResponse.

        描述。

        :param description: The description of this UpgradeCbhInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def task_id(self):
        r"""Gets the task_id of this UpgradeCbhInstanceResponse.

        任务 id。

        :return: The task_id of this UpgradeCbhInstanceResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpgradeCbhInstanceResponse.

        任务 id。

        :param task_id: The task_id of this UpgradeCbhInstanceResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def order_id(self):
        r"""Gets the order_id of this UpgradeCbhInstanceResponse.

        订单 id。

        :return: The order_id of this UpgradeCbhInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this UpgradeCbhInstanceResponse.

        订单 id。

        :param order_id: The order_id of this UpgradeCbhInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, UpgradeCbhInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
