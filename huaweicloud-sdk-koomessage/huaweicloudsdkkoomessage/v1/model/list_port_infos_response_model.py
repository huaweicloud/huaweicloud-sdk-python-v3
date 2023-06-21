# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortInfosResponseModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'PageOffSet',
        'data': 'list[ListPortInfosResponseModelData]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'data': 'data'
    }

    def __init__(self, page_info=None, data=None):
        """ListPortInfosResponseModel

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.PageOffSet`
        :param data: 请求成功返回的数据。
        :type data: list[:class:`huaweicloudsdkkoomessage.v1.ListPortInfosResponseModelData`]
        """
        
        

        self._page_info = None
        self._data = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if data is not None:
            self.data = data

    @property
    def page_info(self):
        """Gets the page_info of this ListPortInfosResponseModel.

        :return: The page_info of this ListPortInfosResponseModel.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.PageOffSet`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPortInfosResponseModel.

        :param page_info: The page_info of this ListPortInfosResponseModel.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.PageOffSet`
        """
        self._page_info = page_info

    @property
    def data(self):
        """Gets the data of this ListPortInfosResponseModel.

        请求成功返回的数据。

        :return: The data of this ListPortInfosResponseModel.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.ListPortInfosResponseModelData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListPortInfosResponseModel.

        请求成功返回的数据。

        :param data: The data of this ListPortInfosResponseModel.
        :type data: list[:class:`huaweicloudsdkkoomessage.v1.ListPortInfosResponseModelData`]
        """
        self._data = data

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
        if not isinstance(other, ListPortInfosResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
