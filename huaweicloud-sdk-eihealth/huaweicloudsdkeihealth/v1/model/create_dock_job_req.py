# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDockJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CreateDrugJobBasicInfo',
        'receptors': 'list[DockingReceptorDto]',
        'ligands': 'list[LigandDto]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptors': 'receptors',
        'ligands': 'ligands'
    }

    def __init__(self, basic_info=None, receptors=None, ligands=None):
        """CreateDockJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param receptors: 受体文件列表
        :type receptors: list[:class:`huaweicloudsdkeihealth.v1.DockingReceptorDto`]
        :param ligands: 配体文件列表，当前仅支持1个
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandDto`]
        """
        
        

        self._basic_info = None
        self._receptors = None
        self._ligands = None
        self.discriminator = None

        self.basic_info = basic_info
        self.receptors = receptors
        self.ligands = ligands

    @property
    def basic_info(self):
        """Gets the basic_info of this CreateDockJobReq.

        :return: The basic_info of this CreateDockJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this CreateDockJobReq.

        :param basic_info: The basic_info of this CreateDockJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def receptors(self):
        """Gets the receptors of this CreateDockJobReq.

        受体文件列表

        :return: The receptors of this CreateDockJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DockingReceptorDto`]
        """
        return self._receptors

    @receptors.setter
    def receptors(self, receptors):
        """Sets the receptors of this CreateDockJobReq.

        受体文件列表

        :param receptors: The receptors of this CreateDockJobReq.
        :type receptors: list[:class:`huaweicloudsdkeihealth.v1.DockingReceptorDto`]
        """
        self._receptors = receptors

    @property
    def ligands(self):
        """Gets the ligands of this CreateDockJobReq.

        配体文件列表，当前仅支持1个

        :return: The ligands of this CreateDockJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LigandDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        """Sets the ligands of this CreateDockJobReq.

        配体文件列表，当前仅支持1个

        :param ligands: The ligands of this CreateDockJobReq.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandDto`]
        """
        self._ligands = ligands

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
        if not isinstance(other, CreateDockJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
