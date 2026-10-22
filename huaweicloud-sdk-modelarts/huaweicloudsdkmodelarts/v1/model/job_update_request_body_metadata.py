# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobUpdateRequestBodyMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'annotation': 'dict(str, str)'
    }

    attribute_map = {
        'annotation': 'annotation'
    }

    def __init__(self, annotation=None):
        r"""JobUpdateRequestBodyMetadata

        The model defined in huaweicloud sdk

        :param annotation: **参数解释**：训练作业高级功能配置。可选取值如下：   - \&quot;jupyter-lab/enable\&quot;: \&quot;true\&quot;（JupyterLab训练应用程序） **约束限制**：不涉及。
        :type annotation: dict(str, str)
        """
        
        

        self._annotation = None
        self.discriminator = None

        if annotation is not None:
            self.annotation = annotation

    @property
    def annotation(self):
        r"""Gets the annotation of this JobUpdateRequestBodyMetadata.

        **参数解释**：训练作业高级功能配置。可选取值如下：   - \"jupyter-lab/enable\": \"true\"（JupyterLab训练应用程序） **约束限制**：不涉及。

        :return: The annotation of this JobUpdateRequestBodyMetadata.
        :rtype: dict(str, str)
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        r"""Sets the annotation of this JobUpdateRequestBodyMetadata.

        **参数解释**：训练作业高级功能配置。可选取值如下：   - \"jupyter-lab/enable\": \"true\"（JupyterLab训练应用程序） **约束限制**：不涉及。

        :param annotation: The annotation of this JobUpdateRequestBodyMetadata.
        :type annotation: dict(str, str)
        """
        self._annotation = annotation

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
        if not isinstance(other, JobUpdateRequestBodyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
