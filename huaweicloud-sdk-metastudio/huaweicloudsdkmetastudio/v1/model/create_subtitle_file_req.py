# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubtitleFileReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'sequence_no': 'int',
        'callback_config': 'CallBackConfig'
    }

    attribute_map = {
        'script_id': 'script_id',
        'sequence_no': 'sequence_no',
        'callback_config': 'callback_config'
    }

    def __init__(self, script_id=None, sequence_no=None, callback_config=None):
        r"""CreateSubtitleFileReq

        The model defined in huaweicloud sdk

        :param script_id: 剧本ID。
        :type script_id: str
        :param sequence_no: 剧本序号。  &gt; * 剧本序号不填生成所有场景的字幕；如果需要生成单场景的字幕，需要填剧本序号。
        :type sequence_no: int
        :param callback_config: 
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        
        

        self._script_id = None
        self._sequence_no = None
        self._callback_config = None
        self.discriminator = None

        if script_id is not None:
            self.script_id = script_id
        if sequence_no is not None:
            self.sequence_no = sequence_no
        if callback_config is not None:
            self.callback_config = callback_config

    @property
    def script_id(self):
        r"""Gets the script_id of this CreateSubtitleFileReq.

        剧本ID。

        :return: The script_id of this CreateSubtitleFileReq.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this CreateSubtitleFileReq.

        剧本ID。

        :param script_id: The script_id of this CreateSubtitleFileReq.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def sequence_no(self):
        r"""Gets the sequence_no of this CreateSubtitleFileReq.

        剧本序号。  > * 剧本序号不填生成所有场景的字幕；如果需要生成单场景的字幕，需要填剧本序号。

        :return: The sequence_no of this CreateSubtitleFileReq.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        r"""Sets the sequence_no of this CreateSubtitleFileReq.

        剧本序号。  > * 剧本序号不填生成所有场景的字幕；如果需要生成单场景的字幕，需要填剧本序号。

        :param sequence_no: The sequence_no of this CreateSubtitleFileReq.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def callback_config(self):
        r"""Gets the callback_config of this CreateSubtitleFileReq.

        :return: The callback_config of this CreateSubtitleFileReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        r"""Sets the callback_config of this CreateSubtitleFileReq.

        :param callback_config: The callback_config of this CreateSubtitleFileReq.
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        self._callback_config = callback_config

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
        if not isinstance(other, CreateSubtitleFileReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
