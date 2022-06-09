# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttributeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sim_card_id': 'int',
        'customer_attribute1': 'str',
        'customer_attribute2': 'str',
        'customer_attribute3': 'str',
        'customer_attribute4': 'str',
        'customer_attribute5': 'str',
        'customer_attribute6': 'str'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'customer_attribute1': 'customer_attribute1',
        'customer_attribute2': 'customer_attribute2',
        'customer_attribute3': 'customer_attribute3',
        'customer_attribute4': 'customer_attribute4',
        'customer_attribute5': 'customer_attribute5',
        'customer_attribute6': 'customer_attribute6'
    }

    def __init__(self, sim_card_id=None, customer_attribute1=None, customer_attribute2=None, customer_attribute3=None, customer_attribute4=None, customer_attribute5=None, customer_attribute6=None):
        """AttributeReq

        The model defined in huaweicloud sdk

        :param sim_card_id: SIM卡标识
        :type sim_card_id: int
        :param customer_attribute1: 自定义属性一
        :type customer_attribute1: str
        :param customer_attribute2: 自定义属性二
        :type customer_attribute2: str
        :param customer_attribute3: 自定义属性三
        :type customer_attribute3: str
        :param customer_attribute4: 自定义属性四
        :type customer_attribute4: str
        :param customer_attribute5: 自定义属性五
        :type customer_attribute5: str
        :param customer_attribute6: 自定义属性六
        :type customer_attribute6: str
        """
        
        

        self._sim_card_id = None
        self._customer_attribute1 = None
        self._customer_attribute2 = None
        self._customer_attribute3 = None
        self._customer_attribute4 = None
        self._customer_attribute5 = None
        self._customer_attribute6 = None
        self.discriminator = None

        self.sim_card_id = sim_card_id
        if customer_attribute1 is not None:
            self.customer_attribute1 = customer_attribute1
        if customer_attribute2 is not None:
            self.customer_attribute2 = customer_attribute2
        if customer_attribute3 is not None:
            self.customer_attribute3 = customer_attribute3
        if customer_attribute4 is not None:
            self.customer_attribute4 = customer_attribute4
        if customer_attribute5 is not None:
            self.customer_attribute5 = customer_attribute5
        if customer_attribute6 is not None:
            self.customer_attribute6 = customer_attribute6

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this AttributeReq.

        SIM卡标识

        :return: The sim_card_id of this AttributeReq.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this AttributeReq.

        SIM卡标识

        :param sim_card_id: The sim_card_id of this AttributeReq.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def customer_attribute1(self):
        """Gets the customer_attribute1 of this AttributeReq.

        自定义属性一

        :return: The customer_attribute1 of this AttributeReq.
        :rtype: str
        """
        return self._customer_attribute1

    @customer_attribute1.setter
    def customer_attribute1(self, customer_attribute1):
        """Sets the customer_attribute1 of this AttributeReq.

        自定义属性一

        :param customer_attribute1: The customer_attribute1 of this AttributeReq.
        :type customer_attribute1: str
        """
        self._customer_attribute1 = customer_attribute1

    @property
    def customer_attribute2(self):
        """Gets the customer_attribute2 of this AttributeReq.

        自定义属性二

        :return: The customer_attribute2 of this AttributeReq.
        :rtype: str
        """
        return self._customer_attribute2

    @customer_attribute2.setter
    def customer_attribute2(self, customer_attribute2):
        """Sets the customer_attribute2 of this AttributeReq.

        自定义属性二

        :param customer_attribute2: The customer_attribute2 of this AttributeReq.
        :type customer_attribute2: str
        """
        self._customer_attribute2 = customer_attribute2

    @property
    def customer_attribute3(self):
        """Gets the customer_attribute3 of this AttributeReq.

        自定义属性三

        :return: The customer_attribute3 of this AttributeReq.
        :rtype: str
        """
        return self._customer_attribute3

    @customer_attribute3.setter
    def customer_attribute3(self, customer_attribute3):
        """Sets the customer_attribute3 of this AttributeReq.

        自定义属性三

        :param customer_attribute3: The customer_attribute3 of this AttributeReq.
        :type customer_attribute3: str
        """
        self._customer_attribute3 = customer_attribute3

    @property
    def customer_attribute4(self):
        """Gets the customer_attribute4 of this AttributeReq.

        自定义属性四

        :return: The customer_attribute4 of this AttributeReq.
        :rtype: str
        """
        return self._customer_attribute4

    @customer_attribute4.setter
    def customer_attribute4(self, customer_attribute4):
        """Sets the customer_attribute4 of this AttributeReq.

        自定义属性四

        :param customer_attribute4: The customer_attribute4 of this AttributeReq.
        :type customer_attribute4: str
        """
        self._customer_attribute4 = customer_attribute4

    @property
    def customer_attribute5(self):
        """Gets the customer_attribute5 of this AttributeReq.

        自定义属性五

        :return: The customer_attribute5 of this AttributeReq.
        :rtype: str
        """
        return self._customer_attribute5

    @customer_attribute5.setter
    def customer_attribute5(self, customer_attribute5):
        """Sets the customer_attribute5 of this AttributeReq.

        自定义属性五

        :param customer_attribute5: The customer_attribute5 of this AttributeReq.
        :type customer_attribute5: str
        """
        self._customer_attribute5 = customer_attribute5

    @property
    def customer_attribute6(self):
        """Gets the customer_attribute6 of this AttributeReq.

        自定义属性六

        :return: The customer_attribute6 of this AttributeReq.
        :rtype: str
        """
        return self._customer_attribute6

    @customer_attribute6.setter
    def customer_attribute6(self, customer_attribute6):
        """Sets the customer_attribute6 of this AttributeReq.

        自定义属性六

        :param customer_attribute6: The customer_attribute6 of this AttributeReq.
        :type customer_attribute6: str
        """
        self._customer_attribute6 = customer_attribute6

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
        if not isinstance(other, AttributeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
