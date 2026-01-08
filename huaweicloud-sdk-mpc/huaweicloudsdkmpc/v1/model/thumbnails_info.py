# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThumbnailsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pic_info': 'list[PicInfo]',
        'output': 'ObsObjInfo',
        'output_name': 'str'
    }

    attribute_map = {
        'pic_info': 'pic_info',
        'output': 'output',
        'output_name': 'output_name'
    }

    def __init__(self, pic_info=None, output=None, output_name=None):
        r"""ThumbnailsInfo

        The model defined in huaweicloud sdk

        :param pic_info: 截图文件信息。 
        :type pic_info: list[:class:`huaweicloudsdkmpc.v1.PicInfo`]
        :param output: 
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param output_name: 截图压缩包名。 
        :type output_name: str
        """
        
        

        self._pic_info = None
        self._output = None
        self._output_name = None
        self.discriminator = None

        if pic_info is not None:
            self.pic_info = pic_info
        if output is not None:
            self.output = output
        if output_name is not None:
            self.output_name = output_name

    @property
    def pic_info(self):
        r"""Gets the pic_info of this ThumbnailsInfo.

        截图文件信息。 

        :return: The pic_info of this ThumbnailsInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.PicInfo`]
        """
        return self._pic_info

    @pic_info.setter
    def pic_info(self, pic_info):
        r"""Sets the pic_info of this ThumbnailsInfo.

        截图文件信息。 

        :param pic_info: The pic_info of this ThumbnailsInfo.
        :type pic_info: list[:class:`huaweicloudsdkmpc.v1.PicInfo`]
        """
        self._pic_info = pic_info

    @property
    def output(self):
        r"""Gets the output of this ThumbnailsInfo.

        :return: The output of this ThumbnailsInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ThumbnailsInfo.

        :param output: The output of this ThumbnailsInfo.
        :type output: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_name(self):
        r"""Gets the output_name of this ThumbnailsInfo.

        截图压缩包名。 

        :return: The output_name of this ThumbnailsInfo.
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        r"""Sets the output_name of this ThumbnailsInfo.

        截图压缩包名。 

        :param output_name: The output_name of this ThumbnailsInfo.
        :type output_name: str
        """
        self._output_name = output_name

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
        if not isinstance(other, ThumbnailsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
