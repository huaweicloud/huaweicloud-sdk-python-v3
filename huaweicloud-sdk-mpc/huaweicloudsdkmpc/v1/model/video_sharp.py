# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoSharp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'execution_order': 'int',
        'amount': 'str'
    }

    attribute_map = {
        'name': 'name',
        'execution_order': 'execution_order',
        'amount': 'amount'
    }

    def __init__(self, name=None, execution_order=None, amount=None):
        r"""VideoSharp

        The model defined in huaweicloud sdk

        :param name: 锐化算法名称\&quot;hw-sharp\&quot;。 
        :type name: str
        :param execution_order: 1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 
        :type execution_order: int
        :param amount: 锐化的程度， 值越大，锐化越强。 
        :type amount: str
        """
        
        

        self._name = None
        self._execution_order = None
        self._amount = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if execution_order is not None:
            self.execution_order = execution_order
        if amount is not None:
            self.amount = amount

    @property
    def name(self):
        r"""Gets the name of this VideoSharp.

        锐化算法名称\"hw-sharp\"。 

        :return: The name of this VideoSharp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VideoSharp.

        锐化算法名称\"hw-sharp\"。 

        :param name: The name of this VideoSharp.
        :type name: str
        """
        self._name = name

    @property
    def execution_order(self):
        r"""Gets the execution_order of this VideoSharp.

        1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 

        :return: The execution_order of this VideoSharp.
        :rtype: int
        """
        return self._execution_order

    @execution_order.setter
    def execution_order(self, execution_order):
        r"""Sets the execution_order of this VideoSharp.

        1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 

        :param execution_order: The execution_order of this VideoSharp.
        :type execution_order: int
        """
        self._execution_order = execution_order

    @property
    def amount(self):
        r"""Gets the amount of this VideoSharp.

        锐化的程度， 值越大，锐化越强。 

        :return: The amount of this VideoSharp.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this VideoSharp.

        锐化的程度， 值越大，锐化越强。 

        :param amount: The amount of this VideoSharp.
        :type amount: str
        """
        self._amount = amount

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
        if not isinstance(other, VideoSharp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
