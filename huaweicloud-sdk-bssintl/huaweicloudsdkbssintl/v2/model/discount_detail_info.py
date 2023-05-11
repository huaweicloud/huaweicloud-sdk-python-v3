# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscountDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'promotion_type': 'str',
        'discount_amount': 'float',
        'promotion_id': 'str',
        'measure_id': 'int'
    }

    attribute_map = {
        'promotion_type': 'promotion_type',
        'discount_amount': 'discount_amount',
        'promotion_id': 'promotion_id',
        'measure_id': 'measure_id'
    }

    def __init__(self, promotion_type=None, discount_amount=None, promotion_id=None, measure_id=None):
        """DiscountDetailInfo

        The model defined in huaweicloud sdk

        :param promotion_type: 折扣类型。 500：代理订购指定折扣 501：代理订购指定减免 502：代理订购指定一口价 600：合同折扣返利 （商履折扣） 601：渠道框架合同折扣 602：专款专用合同折扣（特殊商务合同折扣） 603：线下直签合同折扣 604：电销授权合同折扣 605：商务合同折扣 606：渠道商务合同折扣 607：合作伙伴授权折扣 608：严选商品折扣 610：免单金额 700：促销折扣 （促销，只有包年/包月场景） 800：赠送奖励金
        :type promotion_type: str
        :param discount_amount: 折扣金额。
        :type discount_amount: float
        :param promotion_id: 折扣类型对应的标识，可为合同ID或商务ID。
        :type promotion_id: str
        :param measure_id: 金额单位，1:元 3：分，默认3
        :type measure_id: int
        """
        
        

        self._promotion_type = None
        self._discount_amount = None
        self._promotion_id = None
        self._measure_id = None
        self.discriminator = None

        if promotion_type is not None:
            self.promotion_type = promotion_type
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def promotion_type(self):
        """Gets the promotion_type of this DiscountDetailInfo.

        折扣类型。 500：代理订购指定折扣 501：代理订购指定减免 502：代理订购指定一口价 600：合同折扣返利 （商履折扣） 601：渠道框架合同折扣 602：专款专用合同折扣（特殊商务合同折扣） 603：线下直签合同折扣 604：电销授权合同折扣 605：商务合同折扣 606：渠道商务合同折扣 607：合作伙伴授权折扣 608：严选商品折扣 610：免单金额 700：促销折扣 （促销，只有包年/包月场景） 800：赠送奖励金

        :return: The promotion_type of this DiscountDetailInfo.
        :rtype: str
        """
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        """Sets the promotion_type of this DiscountDetailInfo.

        折扣类型。 500：代理订购指定折扣 501：代理订购指定减免 502：代理订购指定一口价 600：合同折扣返利 （商履折扣） 601：渠道框架合同折扣 602：专款专用合同折扣（特殊商务合同折扣） 603：线下直签合同折扣 604：电销授权合同折扣 605：商务合同折扣 606：渠道商务合同折扣 607：合作伙伴授权折扣 608：严选商品折扣 610：免单金额 700：促销折扣 （促销，只有包年/包月场景） 800：赠送奖励金

        :param promotion_type: The promotion_type of this DiscountDetailInfo.
        :type promotion_type: str
        """
        self._promotion_type = promotion_type

    @property
    def discount_amount(self):
        """Gets the discount_amount of this DiscountDetailInfo.

        折扣金额。

        :return: The discount_amount of this DiscountDetailInfo.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this DiscountDetailInfo.

        折扣金额。

        :param discount_amount: The discount_amount of this DiscountDetailInfo.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def promotion_id(self):
        """Gets the promotion_id of this DiscountDetailInfo.

        折扣类型对应的标识，可为合同ID或商务ID。

        :return: The promotion_id of this DiscountDetailInfo.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """Sets the promotion_id of this DiscountDetailInfo.

        折扣类型对应的标识，可为合同ID或商务ID。

        :param promotion_id: The promotion_id of this DiscountDetailInfo.
        :type promotion_id: str
        """
        self._promotion_id = promotion_id

    @property
    def measure_id(self):
        """Gets the measure_id of this DiscountDetailInfo.

        金额单位，1:元 3：分，默认3

        :return: The measure_id of this DiscountDetailInfo.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this DiscountDetailInfo.

        金额单位，1:元 3：分，默认3

        :param measure_id: The measure_id of this DiscountDetailInfo.
        :type measure_id: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, DiscountDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
