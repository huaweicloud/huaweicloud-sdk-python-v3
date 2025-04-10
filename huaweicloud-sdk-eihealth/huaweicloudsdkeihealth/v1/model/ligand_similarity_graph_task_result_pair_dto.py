# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LigandSimilarityGraphTaskResultPairDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ligands': 'list[str]',
        'success': 'bool',
        'similarity': 'float',
        'reason': 'str'
    }

    attribute_map = {
        'ligands': 'ligands',
        'success': 'success',
        'similarity': 'similarity',
        'reason': 'reason'
    }

    def __init__(self, ligands=None, success=None, similarity=None, reason=None):
        r"""LigandSimilarityGraphTaskResultPairDto

        The model defined in huaweicloud sdk

        :param ligands: 两个配体名称
        :type ligands: list[str]
        :param success: 相似度计算是否成功
        :type success: bool
        :param similarity: 配体对之间的相似度
        :type similarity: float
        :param reason: 相似度计算失败的理由
        :type reason: str
        """
        
        

        self._ligands = None
        self._success = None
        self._similarity = None
        self._reason = None
        self.discriminator = None

        if ligands is not None:
            self.ligands = ligands
        self.success = success
        if similarity is not None:
            self.similarity = similarity
        if reason is not None:
            self.reason = reason

    @property
    def ligands(self):
        r"""Gets the ligands of this LigandSimilarityGraphTaskResultPairDto.

        两个配体名称

        :return: The ligands of this LigandSimilarityGraphTaskResultPairDto.
        :rtype: list[str]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this LigandSimilarityGraphTaskResultPairDto.

        两个配体名称

        :param ligands: The ligands of this LigandSimilarityGraphTaskResultPairDto.
        :type ligands: list[str]
        """
        self._ligands = ligands

    @property
    def success(self):
        r"""Gets the success of this LigandSimilarityGraphTaskResultPairDto.

        相似度计算是否成功

        :return: The success of this LigandSimilarityGraphTaskResultPairDto.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this LigandSimilarityGraphTaskResultPairDto.

        相似度计算是否成功

        :param success: The success of this LigandSimilarityGraphTaskResultPairDto.
        :type success: bool
        """
        self._success = success

    @property
    def similarity(self):
        r"""Gets the similarity of this LigandSimilarityGraphTaskResultPairDto.

        配体对之间的相似度

        :return: The similarity of this LigandSimilarityGraphTaskResultPairDto.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        r"""Sets the similarity of this LigandSimilarityGraphTaskResultPairDto.

        配体对之间的相似度

        :param similarity: The similarity of this LigandSimilarityGraphTaskResultPairDto.
        :type similarity: float
        """
        self._similarity = similarity

    @property
    def reason(self):
        r"""Gets the reason of this LigandSimilarityGraphTaskResultPairDto.

        相似度计算失败的理由

        :return: The reason of this LigandSimilarityGraphTaskResultPairDto.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this LigandSimilarityGraphTaskResultPairDto.

        相似度计算失败的理由

        :param reason: The reason of this LigandSimilarityGraphTaskResultPairDto.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, LigandSimilarityGraphTaskResultPairDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
