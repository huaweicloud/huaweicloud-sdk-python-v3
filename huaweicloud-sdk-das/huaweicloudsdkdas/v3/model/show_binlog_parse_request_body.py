# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBinlogParseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'cur_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, file_name=None, cur_page=None, per_page=None):
        r"""ShowBinlogParseRequestBody

        The model defined in huaweicloud sdk

        :param file_name: binlog文件名称
        :type file_name: str
        :param cur_page: 页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        """
        
        

        self._file_name = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.file_name = file_name
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def file_name(self):
        r"""Gets the file_name of this ShowBinlogParseRequestBody.

        binlog文件名称

        :return: The file_name of this ShowBinlogParseRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ShowBinlogParseRequestBody.

        binlog文件名称

        :param file_name: The file_name of this ShowBinlogParseRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ShowBinlogParseRequestBody.

        页码

        :return: The cur_page of this ShowBinlogParseRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ShowBinlogParseRequestBody.

        页码

        :param cur_page: The cur_page of this ShowBinlogParseRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ShowBinlogParseRequestBody.

        每页记录数

        :return: The per_page of this ShowBinlogParseRequestBody.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ShowBinlogParseRequestBody.

        每页记录数

        :param per_page: The per_page of this ShowBinlogParseRequestBody.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ShowBinlogParseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
