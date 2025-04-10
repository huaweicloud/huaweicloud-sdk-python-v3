# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScoreRequestModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'works_id': 'int',
        'score': 'float',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'works_id': 'works_id',
        'score': 'score',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, works_id=None, score=None, status=None, message=None):
        r"""UpdateScoreRequestModel

        The model defined in huaweicloud sdk

        :param works_id: 作品ID，大赛平台提供，可以通过接口[ListCompetitionWorks](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;CodeCraft&amp;api&#x3D;ListCompetitionWorks)查询作品ID
        :type works_id: int
        :param score: 作品分数，作品状态为failed时传-1，计算长度时包括小数点，小数点后面最多保留四位
        :type score: float
        :param status: 作品状态success|failed。判题时，需要对上传作品进行检查，当作品不符合要求时，应该返回failed，并将提示信息通过 message显示出来
        :type status: str
        :param message: 作品描述信息
        :type message: str
        """
        
        

        self._works_id = None
        self._score = None
        self._status = None
        self._message = None
        self.discriminator = None

        self.works_id = works_id
        self.score = score
        self.status = status
        if message is not None:
            self.message = message

    @property
    def works_id(self):
        r"""Gets the works_id of this UpdateScoreRequestModel.

        作品ID，大赛平台提供，可以通过接口[ListCompetitionWorks](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=CodeCraft&api=ListCompetitionWorks)查询作品ID

        :return: The works_id of this UpdateScoreRequestModel.
        :rtype: int
        """
        return self._works_id

    @works_id.setter
    def works_id(self, works_id):
        r"""Sets the works_id of this UpdateScoreRequestModel.

        作品ID，大赛平台提供，可以通过接口[ListCompetitionWorks](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=CodeCraft&api=ListCompetitionWorks)查询作品ID

        :param works_id: The works_id of this UpdateScoreRequestModel.
        :type works_id: int
        """
        self._works_id = works_id

    @property
    def score(self):
        r"""Gets the score of this UpdateScoreRequestModel.

        作品分数，作品状态为failed时传-1，计算长度时包括小数点，小数点后面最多保留四位

        :return: The score of this UpdateScoreRequestModel.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this UpdateScoreRequestModel.

        作品分数，作品状态为failed时传-1，计算长度时包括小数点，小数点后面最多保留四位

        :param score: The score of this UpdateScoreRequestModel.
        :type score: float
        """
        self._score = score

    @property
    def status(self):
        r"""Gets the status of this UpdateScoreRequestModel.

        作品状态success|failed。判题时，需要对上传作品进行检查，当作品不符合要求时，应该返回failed，并将提示信息通过 message显示出来

        :return: The status of this UpdateScoreRequestModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateScoreRequestModel.

        作品状态success|failed。判题时，需要对上传作品进行检查，当作品不符合要求时，应该返回failed，并将提示信息通过 message显示出来

        :param status: The status of this UpdateScoreRequestModel.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this UpdateScoreRequestModel.

        作品描述信息

        :return: The message of this UpdateScoreRequestModel.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this UpdateScoreRequestModel.

        作品描述信息

        :param message: The message of this UpdateScoreRequestModel.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, UpdateScoreRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
