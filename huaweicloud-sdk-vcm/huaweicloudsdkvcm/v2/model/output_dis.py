# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputDis:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'data_category': 'str'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'data_category': 'data_category'
    }

    def __init__(self, stream_name=None, data_category=None):
        """OutputDis

        The model defined in huaweicloud sdk

        :param stream_name: DIS通道名。
        :type stream_name: str
        :param data_category: 作业输出数据类别的列表，默认值为[]。有这个列表时，表示希望这个输出结果中存放dataCategory列表内的数据。 取值范围为[FaceImage,OriginImage]。 - FaceImage：表示发送人脸图。 - OriginImage：表示发送原始图。
        :type data_category: str
        """
        
        

        self._stream_name = None
        self._data_category = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if data_category is not None:
            self.data_category = data_category

    @property
    def stream_name(self):
        """Gets the stream_name of this OutputDis.

        DIS通道名。

        :return: The stream_name of this OutputDis.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this OutputDis.

        DIS通道名。

        :param stream_name: The stream_name of this OutputDis.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def data_category(self):
        """Gets the data_category of this OutputDis.

        作业输出数据类别的列表，默认值为[]。有这个列表时，表示希望这个输出结果中存放dataCategory列表内的数据。 取值范围为[FaceImage,OriginImage]。 - FaceImage：表示发送人脸图。 - OriginImage：表示发送原始图。

        :return: The data_category of this OutputDis.
        :rtype: str
        """
        return self._data_category

    @data_category.setter
    def data_category(self, data_category):
        """Sets the data_category of this OutputDis.

        作业输出数据类别的列表，默认值为[]。有这个列表时，表示希望这个输出结果中存放dataCategory列表内的数据。 取值范围为[FaceImage,OriginImage]。 - FaceImage：表示发送人脸图。 - OriginImage：表示发送原始图。

        :param data_category: The data_category of this OutputDis.
        :type data_category: str
        """
        self._data_category = data_category

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
        if not isinstance(other, OutputDis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
