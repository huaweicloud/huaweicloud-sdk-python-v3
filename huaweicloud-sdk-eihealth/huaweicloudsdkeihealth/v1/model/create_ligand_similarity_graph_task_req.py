# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLigandSimilarityGraphTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'ligands': 'list[CreateLigandSimilarityGraphLigandDto]'
    }

    attribute_map = {
        'mode': 'mode',
        'ligands': 'ligands'
    }

    def __init__(self, mode=None, ligands=None):
        r"""CreateLigandSimilarityGraphTaskReq

        The model defined in huaweicloud sdk

        :param mode: 创建配体相似度图的模式：中心模式、自由模式
        :type mode: str
        :param ligands: 配体列表
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.CreateLigandSimilarityGraphLigandDto`]
        """
        
        

        self._mode = None
        self._ligands = None
        self.discriminator = None

        self.mode = mode
        self.ligands = ligands

    @property
    def mode(self):
        r"""Gets the mode of this CreateLigandSimilarityGraphTaskReq.

        创建配体相似度图的模式：中心模式、自由模式

        :return: The mode of this CreateLigandSimilarityGraphTaskReq.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateLigandSimilarityGraphTaskReq.

        创建配体相似度图的模式：中心模式、自由模式

        :param mode: The mode of this CreateLigandSimilarityGraphTaskReq.
        :type mode: str
        """
        self._mode = mode

    @property
    def ligands(self):
        r"""Gets the ligands of this CreateLigandSimilarityGraphTaskReq.

        配体列表

        :return: The ligands of this CreateLigandSimilarityGraphTaskReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CreateLigandSimilarityGraphLigandDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this CreateLigandSimilarityGraphTaskReq.

        配体列表

        :param ligands: The ligands of this CreateLigandSimilarityGraphTaskReq.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.CreateLigandSimilarityGraphLigandDto`]
        """
        self._ligands = ligands

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
        if not isinstance(other, CreateLigandSimilarityGraphTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
