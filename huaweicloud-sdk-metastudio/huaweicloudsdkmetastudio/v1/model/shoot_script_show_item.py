# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShootScriptShowItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence_no': 'int',
        'shoot_script': 'ShootScriptDetail',
        'subtitle_file_info': 'SubtitleFiles',
        'preview_info': 'PreviewInfo'
    }

    attribute_map = {
        'sequence_no': 'sequence_no',
        'shoot_script': 'shoot_script',
        'subtitle_file_info': 'subtitle_file_info',
        'preview_info': 'preview_info'
    }

    def __init__(self, sequence_no=None, shoot_script=None, subtitle_file_info=None, preview_info=None):
        """ShootScriptShowItem

        The model defined in huaweicloud sdk

        :param sequence_no: **参数解释**： 剧本序号。 **约束限制**： 同一个剧本序号不重复。 **默认取值**： 不涉及。
        :type sequence_no: int
        :param shoot_script: 
        :type shoot_script: :class:`huaweicloudsdkmetastudio.v1.ShootScriptDetail`
        :param subtitle_file_info: 
        :type subtitle_file_info: :class:`huaweicloudsdkmetastudio.v1.SubtitleFiles`
        :param preview_info: 
        :type preview_info: :class:`huaweicloudsdkmetastudio.v1.PreviewInfo`
        """
        
        

        self._sequence_no = None
        self._shoot_script = None
        self._subtitle_file_info = None
        self._preview_info = None
        self.discriminator = None

        if sequence_no is not None:
            self.sequence_no = sequence_no
        if shoot_script is not None:
            self.shoot_script = shoot_script
        if subtitle_file_info is not None:
            self.subtitle_file_info = subtitle_file_info
        if preview_info is not None:
            self.preview_info = preview_info

    @property
    def sequence_no(self):
        """Gets the sequence_no of this ShootScriptShowItem.

        **参数解释**： 剧本序号。 **约束限制**： 同一个剧本序号不重复。 **默认取值**： 不涉及。

        :return: The sequence_no of this ShootScriptShowItem.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        """Sets the sequence_no of this ShootScriptShowItem.

        **参数解释**： 剧本序号。 **约束限制**： 同一个剧本序号不重复。 **默认取值**： 不涉及。

        :param sequence_no: The sequence_no of this ShootScriptShowItem.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def shoot_script(self):
        """Gets the shoot_script of this ShootScriptShowItem.

        :return: The shoot_script of this ShootScriptShowItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShootScriptDetail`
        """
        return self._shoot_script

    @shoot_script.setter
    def shoot_script(self, shoot_script):
        """Sets the shoot_script of this ShootScriptShowItem.

        :param shoot_script: The shoot_script of this ShootScriptShowItem.
        :type shoot_script: :class:`huaweicloudsdkmetastudio.v1.ShootScriptDetail`
        """
        self._shoot_script = shoot_script

    @property
    def subtitle_file_info(self):
        """Gets the subtitle_file_info of this ShootScriptShowItem.

        :return: The subtitle_file_info of this ShootScriptShowItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SubtitleFiles`
        """
        return self._subtitle_file_info

    @subtitle_file_info.setter
    def subtitle_file_info(self, subtitle_file_info):
        """Sets the subtitle_file_info of this ShootScriptShowItem.

        :param subtitle_file_info: The subtitle_file_info of this ShootScriptShowItem.
        :type subtitle_file_info: :class:`huaweicloudsdkmetastudio.v1.SubtitleFiles`
        """
        self._subtitle_file_info = subtitle_file_info

    @property
    def preview_info(self):
        """Gets the preview_info of this ShootScriptShowItem.

        :return: The preview_info of this ShootScriptShowItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PreviewInfo`
        """
        return self._preview_info

    @preview_info.setter
    def preview_info(self, preview_info):
        """Sets the preview_info of this ShootScriptShowItem.

        :param preview_info: The preview_info of this ShootScriptShowItem.
        :type preview_info: :class:`huaweicloudsdkmetastudio.v1.PreviewInfo`
        """
        self._preview_info = preview_info

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
        if not isinstance(other, ShootScriptShowItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
