# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateYmlsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edit': 'UpdateYmlsReqEdit',
        'inst_type': 'str'
    }

    attribute_map = {
        'edit': 'edit',
        'inst_type': 'inst_type'
    }

    def __init__(self, edit=None, inst_type=None):
        r"""UpdateYmlsReq

        The model defined in huaweicloud sdk

        :param edit: 
        :type edit: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEdit`
        :param inst_type: 节点类型 目前koosearch集群涉及不同类型的节点。 kos: koosearch的搜索中控节点 kos-doc: koosearch的文档解析节点
        :type inst_type: str
        """
        
        

        self._edit = None
        self._inst_type = None
        self.discriminator = None

        self.edit = edit
        if inst_type is not None:
            self.inst_type = inst_type

    @property
    def edit(self):
        r"""Gets the edit of this UpdateYmlsReq.

        :return: The edit of this UpdateYmlsReq.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEdit`
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        r"""Sets the edit of this UpdateYmlsReq.

        :param edit: The edit of this UpdateYmlsReq.
        :type edit: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEdit`
        """
        self._edit = edit

    @property
    def inst_type(self):
        r"""Gets the inst_type of this UpdateYmlsReq.

        节点类型 目前koosearch集群涉及不同类型的节点。 kos: koosearch的搜索中控节点 kos-doc: koosearch的文档解析节点

        :return: The inst_type of this UpdateYmlsReq.
        :rtype: str
        """
        return self._inst_type

    @inst_type.setter
    def inst_type(self, inst_type):
        r"""Sets the inst_type of this UpdateYmlsReq.

        节点类型 目前koosearch集群涉及不同类型的节点。 kos: koosearch的搜索中控节点 kos-doc: koosearch的文档解析节点

        :param inst_type: The inst_type of this UpdateYmlsReq.
        :type inst_type: str
        """
        self._inst_type = inst_type

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
        if not isinstance(other, UpdateYmlsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
