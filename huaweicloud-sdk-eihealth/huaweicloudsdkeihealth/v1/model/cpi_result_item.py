# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CpiResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smiles': 'str',
        'props': 'list[PropertyValue]',
        'score': 'float'
    }

    attribute_map = {
        'smiles': 'smiles',
        'props': 'props',
        'score': 'score'
    }

    def __init__(self, smiles=None, props=None, score=None):
        """CpiResultItem

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param props: 分子ADMET属性值列表
        :type props: list[:class:`huaweicloudsdkeihealth.v1.PropertyValue`]
        :param score: 分子与蛋白质的打分
        :type score: float
        """
        
        

        self._smiles = None
        self._props = None
        self._score = None
        self.discriminator = None

        self.smiles = smiles
        self.props = props
        self.score = score

    @property
    def smiles(self):
        """Gets the smiles of this CpiResultItem.

        分子SMILES表达式

        :return: The smiles of this CpiResultItem.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this CpiResultItem.

        分子SMILES表达式

        :param smiles: The smiles of this CpiResultItem.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def props(self):
        """Gets the props of this CpiResultItem.

        分子ADMET属性值列表

        :return: The props of this CpiResultItem.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.PropertyValue`]
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this CpiResultItem.

        分子ADMET属性值列表

        :param props: The props of this CpiResultItem.
        :type props: list[:class:`huaweicloudsdkeihealth.v1.PropertyValue`]
        """
        self._props = props

    @property
    def score(self):
        """Gets the score of this CpiResultItem.

        分子与蛋白质的打分

        :return: The score of this CpiResultItem.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this CpiResultItem.

        分子与蛋白质的打分

        :param score: The score of this CpiResultItem.
        :type score: float
        """
        self._score = score

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
        if not isinstance(other, CpiResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
