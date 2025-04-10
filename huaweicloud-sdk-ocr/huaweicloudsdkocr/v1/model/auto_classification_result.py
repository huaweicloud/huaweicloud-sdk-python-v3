# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoClassificationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'AutoClassificationResultStatus',
        'content': 'object',
        'type': 'str',
        'location': 'list[list[int]]',
        'seal_mark': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'content': 'content',
        'type': 'type',
        'location': 'location',
        'seal_mark': 'seal_mark'
    }

    def __init__(self, status=None, content=None, type=None, location=None, seal_mark=None):
        r"""AutoClassificationResult

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdkocr.v1.AutoClassificationResultStatus`
        :param content: 对应票证具体结构化识别的结果。 
        :type content: object
        :param type: 对应票证的类别。         
        :type type: str
        :param location: 票证的区域位置信息，列表形式，包含票证区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param seal_mark: 对应票证中是否含有印章。可选值包括： -  true：该票证中含有印章。 -  false：该票证中不含有印章。 
        :type seal_mark: bool
        """
        
        

        self._status = None
        self._content = None
        self._type = None
        self._location = None
        self._seal_mark = None
        self.discriminator = None

        self.status = status
        self.content = content
        self.type = type
        self.location = location
        if seal_mark is not None:
            self.seal_mark = seal_mark

    @property
    def status(self):
        r"""Gets the status of this AutoClassificationResult.

        :return: The status of this AutoClassificationResult.
        :rtype: :class:`huaweicloudsdkocr.v1.AutoClassificationResultStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AutoClassificationResult.

        :param status: The status of this AutoClassificationResult.
        :type status: :class:`huaweicloudsdkocr.v1.AutoClassificationResultStatus`
        """
        self._status = status

    @property
    def content(self):
        r"""Gets the content of this AutoClassificationResult.

        对应票证具体结构化识别的结果。 

        :return: The content of this AutoClassificationResult.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AutoClassificationResult.

        对应票证具体结构化识别的结果。 

        :param content: The content of this AutoClassificationResult.
        :type content: object
        """
        self._content = content

    @property
    def type(self):
        r"""Gets the type of this AutoClassificationResult.

        对应票证的类别。         

        :return: The type of this AutoClassificationResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AutoClassificationResult.

        对应票证的类别。         

        :param type: The type of this AutoClassificationResult.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        r"""Gets the location of this AutoClassificationResult.

        票证的区域位置信息，列表形式，包含票证区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this AutoClassificationResult.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this AutoClassificationResult.

        票证的区域位置信息，列表形式，包含票证区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this AutoClassificationResult.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def seal_mark(self):
        r"""Gets the seal_mark of this AutoClassificationResult.

        对应票证中是否含有印章。可选值包括： -  true：该票证中含有印章。 -  false：该票证中不含有印章。 

        :return: The seal_mark of this AutoClassificationResult.
        :rtype: bool
        """
        return self._seal_mark

    @seal_mark.setter
    def seal_mark(self, seal_mark):
        r"""Sets the seal_mark of this AutoClassificationResult.

        对应票证中是否含有印章。可选值包括： -  true：该票证中含有印章。 -  false：该票证中不含有印章。 

        :param seal_mark: The seal_mark of this AutoClassificationResult.
        :type seal_mark: bool
        """
        self._seal_mark = seal_mark

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
        if not isinstance(other, AutoClassificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
