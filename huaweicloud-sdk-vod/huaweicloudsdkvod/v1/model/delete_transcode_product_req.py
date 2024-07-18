# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTranscodeProductReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'delete_type': 'str',
        'delete_infos': 'list[ProductGroupInfo]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'delete_type': 'delete_type',
        'delete_infos': 'delete_infos'
    }

    def __init__(self, asset_id=None, delete_type=None, delete_infos=None):
        """DeleteTranscodeProductReq

        The model defined in huaweicloud sdk

        :param asset_id: 媒资Id
        :type asset_id: str
        :param delete_type: GROUP：模板组级删除。 PRODUCT：产物级删除
        :type delete_type: str
        :param delete_infos: 删除的产物信息
        :type delete_infos: list[:class:`huaweicloudsdkvod.v1.ProductGroupInfo`]
        """
        
        

        self._asset_id = None
        self._delete_type = None
        self._delete_infos = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if delete_type is not None:
            self.delete_type = delete_type
        if delete_infos is not None:
            self.delete_infos = delete_infos

    @property
    def asset_id(self):
        """Gets the asset_id of this DeleteTranscodeProductReq.

        媒资Id

        :return: The asset_id of this DeleteTranscodeProductReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this DeleteTranscodeProductReq.

        媒资Id

        :param asset_id: The asset_id of this DeleteTranscodeProductReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def delete_type(self):
        """Gets the delete_type of this DeleteTranscodeProductReq.

        GROUP：模板组级删除。 PRODUCT：产物级删除

        :return: The delete_type of this DeleteTranscodeProductReq.
        :rtype: str
        """
        return self._delete_type

    @delete_type.setter
    def delete_type(self, delete_type):
        """Sets the delete_type of this DeleteTranscodeProductReq.

        GROUP：模板组级删除。 PRODUCT：产物级删除

        :param delete_type: The delete_type of this DeleteTranscodeProductReq.
        :type delete_type: str
        """
        self._delete_type = delete_type

    @property
    def delete_infos(self):
        """Gets the delete_infos of this DeleteTranscodeProductReq.

        删除的产物信息

        :return: The delete_infos of this DeleteTranscodeProductReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ProductGroupInfo`]
        """
        return self._delete_infos

    @delete_infos.setter
    def delete_infos(self, delete_infos):
        """Sets the delete_infos of this DeleteTranscodeProductReq.

        删除的产物信息

        :param delete_infos: The delete_infos of this DeleteTranscodeProductReq.
        :type delete_infos: list[:class:`huaweicloudsdkvod.v1.ProductGroupInfo`]
        """
        self._delete_infos = delete_infos

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
        if not isinstance(other, DeleteTranscodeProductReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
