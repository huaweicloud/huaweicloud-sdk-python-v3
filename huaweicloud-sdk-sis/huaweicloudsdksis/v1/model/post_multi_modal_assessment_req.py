# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostMultiModalAssessmentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'MultiModalConfig',
        'video_data': 'str',
        'ref_text': 'str'
    }

    attribute_map = {
        'config': 'config',
        'video_data': 'video_data',
        'ref_text': 'ref_text'
    }

    def __init__(self, config=None, video_data=None, ref_text=None):
        """PostMultiModalAssessmentReq

        The model defined in huaweicloud sdk

        :param config: 
        :type config: :class:`huaweicloudsdksis.v1.MultiModalConfig`
        :param video_data: 视频数据，Base64编码，要求Base64编码后大小不超过10M。  注意评测接口使用次数定义为：每8秒的视频作为一次，不足8秒按一次计算。例如传入4秒或8秒的视频，都算作使用一次，传入9秒的视频则视为调用2次。
        :type video_data: str
        :param ref_text: 被评估视频和语音数据对应的试题文本，长度不可超过256字节。
        :type ref_text: str
        """
        
        

        self._config = None
        self._video_data = None
        self._ref_text = None
        self.discriminator = None

        self.config = config
        self.video_data = video_data
        self.ref_text = ref_text

    @property
    def config(self):
        """Gets the config of this PostMultiModalAssessmentReq.

        :return: The config of this PostMultiModalAssessmentReq.
        :rtype: :class:`huaweicloudsdksis.v1.MultiModalConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PostMultiModalAssessmentReq.

        :param config: The config of this PostMultiModalAssessmentReq.
        :type config: :class:`huaweicloudsdksis.v1.MultiModalConfig`
        """
        self._config = config

    @property
    def video_data(self):
        """Gets the video_data of this PostMultiModalAssessmentReq.

        视频数据，Base64编码，要求Base64编码后大小不超过10M。  注意评测接口使用次数定义为：每8秒的视频作为一次，不足8秒按一次计算。例如传入4秒或8秒的视频，都算作使用一次，传入9秒的视频则视为调用2次。

        :return: The video_data of this PostMultiModalAssessmentReq.
        :rtype: str
        """
        return self._video_data

    @video_data.setter
    def video_data(self, video_data):
        """Sets the video_data of this PostMultiModalAssessmentReq.

        视频数据，Base64编码，要求Base64编码后大小不超过10M。  注意评测接口使用次数定义为：每8秒的视频作为一次，不足8秒按一次计算。例如传入4秒或8秒的视频，都算作使用一次，传入9秒的视频则视为调用2次。

        :param video_data: The video_data of this PostMultiModalAssessmentReq.
        :type video_data: str
        """
        self._video_data = video_data

    @property
    def ref_text(self):
        """Gets the ref_text of this PostMultiModalAssessmentReq.

        被评估视频和语音数据对应的试题文本，长度不可超过256字节。

        :return: The ref_text of this PostMultiModalAssessmentReq.
        :rtype: str
        """
        return self._ref_text

    @ref_text.setter
    def ref_text(self, ref_text):
        """Sets the ref_text of this PostMultiModalAssessmentReq.

        被评估视频和语音数据对应的试题文本，长度不可超过256字节。

        :param ref_text: The ref_text of this PostMultiModalAssessmentReq.
        :type ref_text: str
        """
        self._ref_text = ref_text

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
        if not isinstance(other, PostMultiModalAssessmentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
