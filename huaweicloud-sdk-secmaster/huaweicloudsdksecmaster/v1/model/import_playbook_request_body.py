# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportPlaybookRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upload_file': 'file',
        'upload_model': 'str'
    }

    attribute_map = {
        'upload_file': 'uploadFile',
        'upload_model': 'upload_model'
    }

    def __init__(self, upload_file=None, upload_model=None):
        r"""ImportPlaybookRequestBody

        The model defined in huaweicloud sdk

        :param upload_file: 导入文件
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param upload_model: 剧本文件上传模式 import 剧本上传导入 verify 剧本上传校验
        :type upload_model: str
        """
        
        

        self._upload_file = None
        self._upload_model = None
        self.discriminator = None

        self.upload_file = upload_file
        if upload_model is not None:
            self.upload_model = upload_model

    @property
    def upload_file(self):
        r"""Gets the upload_file of this ImportPlaybookRequestBody.

        导入文件

        :return: The upload_file of this ImportPlaybookRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._upload_file

    @upload_file.setter
    def upload_file(self, upload_file):
        r"""Sets the upload_file of this ImportPlaybookRequestBody.

        导入文件

        :param upload_file: The upload_file of this ImportPlaybookRequestBody.
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._upload_file = upload_file

    @property
    def upload_model(self):
        r"""Gets the upload_model of this ImportPlaybookRequestBody.

        剧本文件上传模式 import 剧本上传导入 verify 剧本上传校验

        :return: The upload_model of this ImportPlaybookRequestBody.
        :rtype: str
        """
        return self._upload_model

    @upload_model.setter
    def upload_model(self, upload_model):
        r"""Sets the upload_model of this ImportPlaybookRequestBody.

        剧本文件上传模式 import 剧本上传导入 verify 剧本上传校验

        :param upload_model: The upload_model of this ImportPlaybookRequestBody.
        :type upload_model: str
        """
        self._upload_model = upload_model

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
        if not isinstance(other, ImportPlaybookRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
