# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chart': 'file',
        'images': 'str'
    }

    attribute_map = {
        'chart': 'chart',
        'images': 'images'
    }

    def __init__(self, chart=None, images=None):
        """CreateAppVersionRequestBody

        The model defined in huaweicloud sdk

        :param chart: chart包。当前仅支持tgz文件格式。
        :type chart: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param images: 应用包含的镜像列表
        :type images: str
        """
        
        

        self._chart = None
        self._images = None
        self.discriminator = None

        self.chart = chart
        if images is not None:
            self.images = images

    @property
    def chart(self):
        """Gets the chart of this CreateAppVersionRequestBody.

        chart包。当前仅支持tgz文件格式。

        :return: The chart of this CreateAppVersionRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this CreateAppVersionRequestBody.

        chart包。当前仅支持tgz文件格式。

        :param chart: The chart of this CreateAppVersionRequestBody.
        :type chart: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._chart = chart

    @property
    def images(self):
        """Gets the images of this CreateAppVersionRequestBody.

        应用包含的镜像列表

        :return: The images of this CreateAppVersionRequestBody.
        :rtype: str
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this CreateAppVersionRequestBody.

        应用包含的镜像列表

        :param images: The images of this CreateAppVersionRequestBody.
        :type images: str
        """
        self._images = images

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
        if not isinstance(other, CreateAppVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
