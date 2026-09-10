# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchTagValueMsg:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg': 'str',
        'code': 'str'
    }

    attribute_map = {
        'msg': 'msg',
        'code': 'code'
    }

    def __init__(self, msg=None, code=None):
        r"""BatchTagValueMsg

        The model defined in huaweicloud sdk

        :param msg: **参数解释：** 返回的结果的msg。 **约束限制：** 不涉及。 
        :type msg: str
        :param code: **参数解释：** 返回的结果的code。 **约束限制：** 不涉及。 
        :type code: str
        """
        
        

        self._msg = None
        self._code = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if code is not None:
            self.code = code

    @property
    def msg(self):
        r"""Gets the msg of this BatchTagValueMsg.

        **参数解释：** 返回的结果的msg。 **约束限制：** 不涉及。 

        :return: The msg of this BatchTagValueMsg.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this BatchTagValueMsg.

        **参数解释：** 返回的结果的msg。 **约束限制：** 不涉及。 

        :param msg: The msg of this BatchTagValueMsg.
        :type msg: str
        """
        self._msg = msg

    @property
    def code(self):
        r"""Gets the code of this BatchTagValueMsg.

        **参数解释：** 返回的结果的code。 **约束限制：** 不涉及。 

        :return: The code of this BatchTagValueMsg.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BatchTagValueMsg.

        **参数解释：** 返回的结果的code。 **约束限制：** 不涉及。 

        :param code: The code of this BatchTagValueMsg.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, BatchTagValueMsg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
