# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJudgementFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str'
    }

    attribute_map = {
        'file_id': 'file_id'
    }

    def __init__(self, file_id=None):
        r"""ShowJudgementFileRequest

        The model defined in huaweicloud sdk

        :param file_id: 文件id，可以从接口[ShowJudgementDetail](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;Classroom&amp;api&#x3D;ShowJudgementDetail)的响应中获取
        :type file_id: str
        """
        
        

        self._file_id = None
        self.discriminator = None

        self.file_id = file_id

    @property
    def file_id(self):
        r"""Gets the file_id of this ShowJudgementFileRequest.

        文件id，可以从接口[ShowJudgementDetail](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=Classroom&api=ShowJudgementDetail)的响应中获取

        :return: The file_id of this ShowJudgementFileRequest.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ShowJudgementFileRequest.

        文件id，可以从接口[ShowJudgementDetail](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=Classroom&api=ShowJudgementDetail)的响应中获取

        :param file_id: The file_id of this ShowJudgementFileRequest.
        :type file_id: str
        """
        self._file_id = file_id

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
        if not isinstance(other, ShowJudgementFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
