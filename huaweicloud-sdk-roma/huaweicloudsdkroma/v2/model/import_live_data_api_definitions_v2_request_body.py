# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportLiveDataApiDefinitionsV2RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extend_mode': 'str',
        'api_mode': 'str',
        'file_name': 'file'
    }

    attribute_map = {
        'extend_mode': 'extend_mode',
        'api_mode': 'api_mode',
        'file_name': 'file_name'
    }

    def __init__(self, extend_mode=None, api_mode=None, file_name=None):
        """ImportLiveDataApiDefinitionsV2RequestBody

        The model defined in huaweicloud sdk

        :param extend_mode: 扩展信息导入模式 - merge：当扩展信息定义冲突时，merge保留原有扩展信息 - override：当扩展信息定义冲突时，override会覆盖原有扩展信息
        :type extend_mode: str
        :param api_mode: 导入模式 - merge：当API信息定义冲突时，merge保留原有API信息 - override：当API信息定义冲突时，override会覆盖原有API信息
        :type api_mode: str
        :param file_name: 导入自定义后端API的请求体，json或yaml格式的文件
        :type file_name: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._extend_mode = None
        self._api_mode = None
        self._file_name = None
        self.discriminator = None

        if extend_mode is not None:
            self.extend_mode = extend_mode
        if api_mode is not None:
            self.api_mode = api_mode
        self.file_name = file_name

    @property
    def extend_mode(self):
        """Gets the extend_mode of this ImportLiveDataApiDefinitionsV2RequestBody.

        扩展信息导入模式 - merge：当扩展信息定义冲突时，merge保留原有扩展信息 - override：当扩展信息定义冲突时，override会覆盖原有扩展信息

        :return: The extend_mode of this ImportLiveDataApiDefinitionsV2RequestBody.
        :rtype: str
        """
        return self._extend_mode

    @extend_mode.setter
    def extend_mode(self, extend_mode):
        """Sets the extend_mode of this ImportLiveDataApiDefinitionsV2RequestBody.

        扩展信息导入模式 - merge：当扩展信息定义冲突时，merge保留原有扩展信息 - override：当扩展信息定义冲突时，override会覆盖原有扩展信息

        :param extend_mode: The extend_mode of this ImportLiveDataApiDefinitionsV2RequestBody.
        :type extend_mode: str
        """
        self._extend_mode = extend_mode

    @property
    def api_mode(self):
        """Gets the api_mode of this ImportLiveDataApiDefinitionsV2RequestBody.

        导入模式 - merge：当API信息定义冲突时，merge保留原有API信息 - override：当API信息定义冲突时，override会覆盖原有API信息

        :return: The api_mode of this ImportLiveDataApiDefinitionsV2RequestBody.
        :rtype: str
        """
        return self._api_mode

    @api_mode.setter
    def api_mode(self, api_mode):
        """Sets the api_mode of this ImportLiveDataApiDefinitionsV2RequestBody.

        导入模式 - merge：当API信息定义冲突时，merge保留原有API信息 - override：当API信息定义冲突时，override会覆盖原有API信息

        :param api_mode: The api_mode of this ImportLiveDataApiDefinitionsV2RequestBody.
        :type api_mode: str
        """
        self._api_mode = api_mode

    @property
    def file_name(self):
        """Gets the file_name of this ImportLiveDataApiDefinitionsV2RequestBody.

        导入自定义后端API的请求体，json或yaml格式的文件

        :return: The file_name of this ImportLiveDataApiDefinitionsV2RequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ImportLiveDataApiDefinitionsV2RequestBody.

        导入自定义后端API的请求体，json或yaml格式的文件

        :param file_name: The file_name of this ImportLiveDataApiDefinitionsV2RequestBody.
        :type file_name: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file_name = file_name

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
        if not isinstance(other, ImportLiveDataApiDefinitionsV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
