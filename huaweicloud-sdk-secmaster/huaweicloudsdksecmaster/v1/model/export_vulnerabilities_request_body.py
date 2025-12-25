# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVulnerabilitiesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_object_filters_form': 'VulnerabilityDataObjectSearch',
        'title': 'list[str]'
    }

    attribute_map = {
        'data_object_filters_form': 'data_object_filters_form',
        'title': 'title'
    }

    def __init__(self, data_object_filters_form=None, title=None):
        r"""ExportVulnerabilitiesRequestBody

        The model defined in huaweicloud sdk

        :param data_object_filters_form: 
        :type data_object_filters_form: :class:`huaweicloudsdksecmaster.v1.VulnerabilityDataObjectSearch`
        :param title: 导出字段
        :type title: list[str]
        """
        
        

        self._data_object_filters_form = None
        self._title = None
        self.discriminator = None

        if data_object_filters_form is not None:
            self.data_object_filters_form = data_object_filters_form
        if title is not None:
            self.title = title

    @property
    def data_object_filters_form(self):
        r"""Gets the data_object_filters_form of this ExportVulnerabilitiesRequestBody.

        :return: The data_object_filters_form of this ExportVulnerabilitiesRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.VulnerabilityDataObjectSearch`
        """
        return self._data_object_filters_form

    @data_object_filters_form.setter
    def data_object_filters_form(self, data_object_filters_form):
        r"""Sets the data_object_filters_form of this ExportVulnerabilitiesRequestBody.

        :param data_object_filters_form: The data_object_filters_form of this ExportVulnerabilitiesRequestBody.
        :type data_object_filters_form: :class:`huaweicloudsdksecmaster.v1.VulnerabilityDataObjectSearch`
        """
        self._data_object_filters_form = data_object_filters_form

    @property
    def title(self):
        r"""Gets the title of this ExportVulnerabilitiesRequestBody.

        导出字段

        :return: The title of this ExportVulnerabilitiesRequestBody.
        :rtype: list[str]
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ExportVulnerabilitiesRequestBody.

        导出字段

        :param title: The title of this ExportVulnerabilitiesRequestBody.
        :type title: list[str]
        """
        self._title = title

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
        if not isinstance(other, ExportVulnerabilitiesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
