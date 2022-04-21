# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvExecutionBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'params': 'list[DynamicConfigInfo]',
        'record_id': 'str'
    }

    attribute_map = {
        'params': 'params',
        'record_id': 'record_id'
    }

    def __init__(self, params=None, record_id=None):
        """EnvExecutionBody

        The model defined in huaweicloud sdk

        :param params: 部署任务执行时传递的参数
        :type params: list[:class:`huaweicloudsdkclouddeploy.v2.DynamicConfigInfo`]
        :param record_id: 部署任务的执行id，可通过record_id回滚至之前的部署状态。选中部署历史执行记录，在URL中获取。
        :type record_id: str
        """
        
        

        self._params = None
        self._record_id = None
        self.discriminator = None

        self.params = params
        if record_id is not None:
            self.record_id = record_id

    @property
    def params(self):
        """Gets the params of this EnvExecutionBody.

        部署任务执行时传递的参数

        :return: The params of this EnvExecutionBody.
        :rtype: list[:class:`huaweicloudsdkclouddeploy.v2.DynamicConfigInfo`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this EnvExecutionBody.

        部署任务执行时传递的参数

        :param params: The params of this EnvExecutionBody.
        :type params: list[:class:`huaweicloudsdkclouddeploy.v2.DynamicConfigInfo`]
        """
        self._params = params

    @property
    def record_id(self):
        """Gets the record_id of this EnvExecutionBody.

        部署任务的执行id，可通过record_id回滚至之前的部署状态。选中部署历史执行记录，在URL中获取。

        :return: The record_id of this EnvExecutionBody.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this EnvExecutionBody.

        部署任务的执行id，可通过record_id回滚至之前的部署状态。选中部署历史执行记录，在URL中获取。

        :param record_id: The record_id of this EnvExecutionBody.
        :type record_id: str
        """
        self._record_id = record_id

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
        if not isinstance(other, EnvExecutionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
