# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFlinkJobsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zip_file': 'str',
        'is_cover': 'bool'
    }

    attribute_map = {
        'zip_file': 'zip_file',
        'is_cover': 'is_cover'
    }

    def __init__(self, zip_file=None, is_cover=None):
        r"""ImportFlinkJobsRequestBody

        The model defined in huaweicloud sdk

        :param zip_file: OBS上导入作业zip文件路径，支持填写目录，导入目录下所有zip文件。
        :type zip_file: str
        :param is_cover: 若导入作业中存在与服务已有作业同名情况，是否将服务中已有作业覆盖。
        :type is_cover: bool
        """
        
        

        self._zip_file = None
        self._is_cover = None
        self.discriminator = None

        self.zip_file = zip_file
        if is_cover is not None:
            self.is_cover = is_cover

    @property
    def zip_file(self):
        r"""Gets the zip_file of this ImportFlinkJobsRequestBody.

        OBS上导入作业zip文件路径，支持填写目录，导入目录下所有zip文件。

        :return: The zip_file of this ImportFlinkJobsRequestBody.
        :rtype: str
        """
        return self._zip_file

    @zip_file.setter
    def zip_file(self, zip_file):
        r"""Sets the zip_file of this ImportFlinkJobsRequestBody.

        OBS上导入作业zip文件路径，支持填写目录，导入目录下所有zip文件。

        :param zip_file: The zip_file of this ImportFlinkJobsRequestBody.
        :type zip_file: str
        """
        self._zip_file = zip_file

    @property
    def is_cover(self):
        r"""Gets the is_cover of this ImportFlinkJobsRequestBody.

        若导入作业中存在与服务已有作业同名情况，是否将服务中已有作业覆盖。

        :return: The is_cover of this ImportFlinkJobsRequestBody.
        :rtype: bool
        """
        return self._is_cover

    @is_cover.setter
    def is_cover(self, is_cover):
        r"""Sets the is_cover of this ImportFlinkJobsRequestBody.

        若导入作业中存在与服务已有作业同名情况，是否将服务中已有作业覆盖。

        :param is_cover: The is_cover of this ImportFlinkJobsRequestBody.
        :type is_cover: bool
        """
        self._is_cover = is_cover

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
        if not isinstance(other, ImportFlinkJobsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
