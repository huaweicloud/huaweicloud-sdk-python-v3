# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtlasFullTextResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity': 'AtlasEntityHeader',
        'score': 'float'
    }

    attribute_map = {
        'entity': 'entity',
        'score': 'score'
    }

    def __init__(self, entity=None, score=None):
        r"""AtlasFullTextResult

        The model defined in huaweicloud sdk

        :param entity: 
        :type entity: :class:`huaweicloudsdkdataartsstudio.v1.AtlasEntityHeader`
        :param score: 数值
        :type score: float
        """
        
        

        self._entity = None
        self._score = None
        self.discriminator = None

        if entity is not None:
            self.entity = entity
        if score is not None:
            self.score = score

    @property
    def entity(self):
        r"""Gets the entity of this AtlasFullTextResult.

        :return: The entity of this AtlasFullTextResult.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AtlasEntityHeader`
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        r"""Sets the entity of this AtlasFullTextResult.

        :param entity: The entity of this AtlasFullTextResult.
        :type entity: :class:`huaweicloudsdkdataartsstudio.v1.AtlasEntityHeader`
        """
        self._entity = entity

    @property
    def score(self):
        r"""Gets the score of this AtlasFullTextResult.

        数值

        :return: The score of this AtlasFullTextResult.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this AtlasFullTextResult.

        数值

        :param score: The score of this AtlasFullTextResult.
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
        if not isinstance(other, AtlasFullTextResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
