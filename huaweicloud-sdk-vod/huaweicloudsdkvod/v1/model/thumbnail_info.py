# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThumbnailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample': 'list[ThumbnailRsp]',
        'dots': 'list[ThumbnailRsp]',
        'quantity': 'list[ThumbnailRsp]',
        'exec_desc': 'str',
        'thumbnail_status': 'str'
    }

    attribute_map = {
        'sample': 'sample',
        'dots': 'dots',
        'quantity': 'quantity',
        'exec_desc': 'exec_desc',
        'thumbnail_status': 'thumbnail_status'
    }

    def __init__(self, sample=None, dots=None, quantity=None, exec_desc=None, thumbnail_status=None):
        r"""ThumbnailInfo

        The model defined in huaweicloud sdk

        :param sample: 视频截图信息。
        :type sample: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        :param dots: 
        :type dots: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        :param quantity: 视频截图信息，截图类型为数量。
        :type quantity: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        :param exec_desc: 执行情况描述。
        :type exec_desc: str
        :param thumbnail_status: 截图状态。  取值如下： - UN_THUMBNAIL：未截图 - THUMBNAILING：截图中 - THUMBNAIL_SUCCEED：截图成功 - THUMBNAIL_FAILED：截图失败
        :type thumbnail_status: str
        """
        
        

        self._sample = None
        self._dots = None
        self._quantity = None
        self._exec_desc = None
        self._thumbnail_status = None
        self.discriminator = None

        if sample is not None:
            self.sample = sample
        if dots is not None:
            self.dots = dots
        if quantity is not None:
            self.quantity = quantity
        if exec_desc is not None:
            self.exec_desc = exec_desc
        if thumbnail_status is not None:
            self.thumbnail_status = thumbnail_status

    @property
    def sample(self):
        r"""Gets the sample of this ThumbnailInfo.

        视频截图信息。

        :return: The sample of this ThumbnailInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        r"""Sets the sample of this ThumbnailInfo.

        视频截图信息。

        :param sample: The sample of this ThumbnailInfo.
        :type sample: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        """
        self._sample = sample

    @property
    def dots(self):
        r"""Gets the dots of this ThumbnailInfo.

        :return: The dots of this ThumbnailInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        """
        return self._dots

    @dots.setter
    def dots(self, dots):
        r"""Sets the dots of this ThumbnailInfo.

        :param dots: The dots of this ThumbnailInfo.
        :type dots: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        """
        self._dots = dots

    @property
    def quantity(self):
        r"""Gets the quantity of this ThumbnailInfo.

        视频截图信息，截图类型为数量。

        :return: The quantity of this ThumbnailInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        r"""Sets the quantity of this ThumbnailInfo.

        视频截图信息，截图类型为数量。

        :param quantity: The quantity of this ThumbnailInfo.
        :type quantity: list[:class:`huaweicloudsdkvod.v1.ThumbnailRsp`]
        """
        self._quantity = quantity

    @property
    def exec_desc(self):
        r"""Gets the exec_desc of this ThumbnailInfo.

        执行情况描述。

        :return: The exec_desc of this ThumbnailInfo.
        :rtype: str
        """
        return self._exec_desc

    @exec_desc.setter
    def exec_desc(self, exec_desc):
        r"""Sets the exec_desc of this ThumbnailInfo.

        执行情况描述。

        :param exec_desc: The exec_desc of this ThumbnailInfo.
        :type exec_desc: str
        """
        self._exec_desc = exec_desc

    @property
    def thumbnail_status(self):
        r"""Gets the thumbnail_status of this ThumbnailInfo.

        截图状态。  取值如下： - UN_THUMBNAIL：未截图 - THUMBNAILING：截图中 - THUMBNAIL_SUCCEED：截图成功 - THUMBNAIL_FAILED：截图失败

        :return: The thumbnail_status of this ThumbnailInfo.
        :rtype: str
        """
        return self._thumbnail_status

    @thumbnail_status.setter
    def thumbnail_status(self, thumbnail_status):
        r"""Sets the thumbnail_status of this ThumbnailInfo.

        截图状态。  取值如下： - UN_THUMBNAIL：未截图 - THUMBNAILING：截图中 - THUMBNAIL_SUCCEED：截图成功 - THUMBNAIL_FAILED：截图失败

        :param thumbnail_status: The thumbnail_status of this ThumbnailInfo.
        :type thumbnail_status: str
        """
        self._thumbnail_status = thumbnail_status

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
        if not isinstance(other, ThumbnailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
